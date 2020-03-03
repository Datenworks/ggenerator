from pandas import DataFrame, Series

from src.generators.datatypes import generators_map
from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset
from src.lib.formatters import formatters
from src.lib.writers import writers


class GeneratorsHandler(object):
    """GeneratorsHandler is responsible to integrate
    all the modules, serving like a facade to the user.
    """

    def __init__(self, arguments: dict):
        self.file_path = arguments['config_file']
        self.specification = self.get_valid_specification()

    def get_valid_specification(self):
        config_reader = ConfigurationValidator(self.file_path)
        config = config_reader.get_config()

        if 'datasets' not in config:
            raise ValueError("Malformed specification file")

        datasets = config.get('datasets')
        for key in datasets.keys():
            dataset_validator = ConfigurationDataset(
                id=key,
                size=datasets[key]['size'],
                fields=datasets[key]['fields'],
                format=datasets[key]['format'],
                serializers=datasets[key]['serializers']
            )
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
                file_path = self.write_dataframe(dataframe,
                                                 destination,
                                                 dataset_format)
                file_format = dataset_format['type']
<<<<<<< HEAD
                yield key, file_format, destination
=======
                yield key, file_format, file_path
>>>>>>> origin/feature/s3_serializer

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
                        format_: dict) -> str:
        file_format = format_['type']
        formatter_class = formatters[file_format]
        formatter = formatter_class(specification=format_)

        destination_type = destination['type']
        writer_class = writers[destination_type]
        writer = writer_class(formatter=formatter, specification=destination)

        return writer.write(dataframe=dataframe)
