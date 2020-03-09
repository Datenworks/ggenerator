from pandas import DataFrame, Series

from src.generators.datatypes import get_generators_map
from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset


class BaseHandler(object):

    def valid_specification(self, file_path):
        config_reader = ConfigurationValidator(file_path)
        config = config_reader.get_config()

        if 'datasets' not in config:
            raise ValueError("Don't have any datasets")

        datasets = config.get('datasets')

        if not datasets.keys():
            raise ValueError("Malformed specification file")

        for key in datasets.keys():
            dataset_validator = ConfigurationDataset(
                id=key,
                size=datasets[key].get('size'),
                fields=datasets[key].get('fields'),
                format=datasets[key].get('format'),
                serializers=datasets[key].get('serializers')
            )
            try:
                dataset_validator.is_valid()
            except ValueError as e:
                raise ValueError("Malformed specification file: ", e)

        return config

    def generate_dataframe(self, specification: dict, size) -> DataFrame:
        size = size
        fields = specification['fields']
        locale = specification['locale']
        generators_map = get_generators_map(locale)

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
