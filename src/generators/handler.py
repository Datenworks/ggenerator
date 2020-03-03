from pandas import DataFrame, Series

from src.generators.datatypes import generators_map
from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset
from src.lib.writers import writers


class GeneratorsHandler(object):
    """GeneratorsHandler is responsible to integrate
    all the modules, serving like a facade to the user.
    """

    def __init__(self, arguments: dict):
        self.file_path = arguments['config_file']
        self.specification = self.get_valid_specification()
        self.writers = writers

    def get_valid_specification(self):
        config_reader = ConfigurationValidator(self.file_path)
        config = config_reader.get_config()

        if 'datasets' not in config:
            raise ValueError("Don't have any datasets")

        datasets = config.get('datasets')
        for key in datasets.keys():
            dataset_validator = ConfigurationDataset(
                id=key,
                size=datasets[key]['size'],
                fields=datasets[key]['fields'],
                format=datasets[key].get('format'),
                serializers=datasets[key]['serializers']
            )
            if dataset_validator.size <= 0:
                raise ValueError("'size' must be bigger than 0")
            if dataset_validator.is_valid() is False:
                raise ValueError("Malformed specification file")

        return config

    def generate(self):
        datasets = self.specification.get('datasets')
        for key in datasets.keys():
            dataset = datasets[key]
            dataset_format = dataset['format']
            dataframe = self.generate_dataframe(dataset)
            for destination in dataset['serializers']['to']:
                file_format, file_path = self.write_dataframe(dataframe,
                                                              destination,
                                                              dataset_format)
                yield key, file_format, file_path

    def generate_dataframe(self, specification: dict) -> DataFrame:
        size = specification['size']
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

    def write_dataframe(self,
                        dataframe: DataFrame,
                        destination: dict,
                        dataset_format: dict) -> (str, str):
        file_format = dataset_format['type']
        file_path = destination['uri']
        writer = self.writers[file_format]()
        writer.write(dataframe=dataframe,
                     file_path=file_path,
                     **dataset_format.get("options", {}))
        return file_format, file_path
