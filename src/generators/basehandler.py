import json

from alive_progress import alive_bar
from pandas import DataFrame, Series

from src.lib.config import general_rules, datetime_rules
from src.lib.config.fields import FieldsConfiguration
from src.lib.config.formatters import FormattersConfiguration
from src.lib.config.inspector import ConfigurationInpector
from src.lib.config.serializers import SerializersConfiguration
from src.generators.datatypes import Metadata


class BaseHandler(object):
    def __init__(self):
        self.inspector = ConfigurationInpector()

    def __validate(self, clazz, iterable, trace, **kwargs):
        for item in iterable:
            try:
                rules = clazz.get_rules(item, **kwargs)
            except ValueError as err:
                type_ = item.get('type', '')
                name = item.get('name', type_)
                message = (f"Key {trace}{name} ({err})")
                raise ValueError(message)
            self.inspector.inspect_rules(rules=rules['required'],
                                         configuration=item)
            self.inspector.inspect_rules(rules=rules['optional'],
                                         configuration=item,
                                         optional=True)

    def __validate_fields(self, dataset, trace):
        fields = dataset['fields']
        self.__validate(clazz=FieldsConfiguration,
                        iterable=fields,
                        locale=dataset['locale'],
                        trace=f"{trace}fields.")

    def __validate_format(self, dataset, trace):
        self.__validate(clazz=FormattersConfiguration,
                        iterable=[dataset['format']],
                        trace=f"{trace}format.")

    def __validate_serializers(self, dataset, trace):
        serializers = dataset['serializers']['to']
        self.__validate(clazz=SerializersConfiguration,
                        iterable=serializers,
                        trace=f"{trace}serializers.to.")

    def valid_specification(self, file_path):
        with open(file_path, 'r') as file:
            try:
                configuration = json.loads(file.read())
            except Exception:
                raise ValueError("Malformed specification file/blank field")

        self.inspector.inspect_rules(rules=general_rules,
                                     configuration=configuration)

        for dataset_key in configuration['datasets']:
            dataset = configuration['datasets'][dataset_key]

            trace = f"datasets.{dataset_key}."
            self.__validate_fields(dataset, trace)
            self.__validate_format(dataset, trace)
            self.__validate_serializers(dataset, trace)

        for dataset_key in configuration['datasets']:
            has_datetime = False
            dataset = configuration['datasets'][dataset_key]
            for field in dataset['fields']:
                if field.get('type') == 'date_time':
                    has_datetime = True
                    break
            if has_datetime:
                self.inspector \
                    .inspect_rules(rules=datetime_rules,
                                   configuration=dataset)

        return configuration

    def generate_dataframe(self, specification: dict, size) -> DataFrame:
        fields = specification['fields']
        locale = specification['locale']
        generators_map = Metadata(locale=locale).get_generators_map()

        dataframe = DataFrame()
        for field in fields:
            field_name = field['name']
            field_type = field['type']
            field_arguments = field['generator']

            generator_class = generators_map[field_type]['type']
            generator = generator_class(**field_arguments)

            with alive_bar(size) as bar:
                # E731 do not assign a lambda expression, use a def
                def progress(): bar(text=f"ggenerating {field_name}")

                series = Series(generator.generate_records(num_of_records=size,
                                                           progress=progress))

            dataframe[field_name] = series.values

        return dataframe
