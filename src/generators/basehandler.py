from pandas import DataFrame, Series

from src.generators.datatypes import generators_map
from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset


class BaseHandler(object):

    def valid_specification(self, file_path):
        config_reader = ConfigurationValidator(file_path)
        config = config_reader.get_config()

        if 'datasets' not in config:
            raise ValueError("Malformed specification file")

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
            if dataset_validator.is_valid() is False:
                raise ValueError("Malformed specification file")

        return config

    def generate_dataframe(self, specification: dict, size) -> DataFrame:
        size = size
        fields = specification['fields']

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
