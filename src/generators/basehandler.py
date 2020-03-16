import json

from pandas import DataFrame, Series

from src.lib.config import general_rules
from src.lib.config.fields import FieldsConfiguration
from src.lib.config.formatters import FormattersConfiguration
from src.lib.config.inspector import ConfigurationInpector
from src.lib.config.serializers import SerializersConfiguration
from src.generators.datatypes import Metadata


class BaseHandler(object):
    def __init__(self):
        self.inspector = ConfigurationInpector()

    def __validate(self, clazz, iterable, **kwargs):
        for item in iterable:
            rules = clazz.get_rules(item, **kwargs)
            self.inspector.inspect_rules(rules=rules['required'],
                                         configuration=item)
            self.inspector.inspect_rules(rules=rules['optional'],
                                         configuration=item,
                                         optional=True)

    def __validate_fields(self, dataset):
        fields = dataset['fields']
        self.__validate(clazz=FieldsConfiguration,
                        iterable=fields,
                        locale=dataset['locale'])

    def __validate_format(self, dataset):
        self.__validate(clazz=FormattersConfiguration,
                        iterable=[dataset['format']])

    def __validate_serializers(self, dataset):
        serializers = dataset['serializers']['to']
        self.__validate(clazz=SerializersConfiguration,
                        iterable=serializers)

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

            self.__validate_fields(dataset)
            self.__validate_format(dataset)
            self.__validate_serializers(dataset)
        return configuration

    def generate_dataframe(self, specification: dict, size) -> DataFrame:
        size = size
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

            series = Series(generator.generate_records(size))

            dataframe[field_name] = series.values

        return dataframe
