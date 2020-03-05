from pandas import DataFrame

from src.lib.formatters import formatters
from src.lib.writers import writers
from src.generators.basehandler import BaseHandler


class GeneratorsHandler(object):

    def __init__(self, arguments: dict):
        self.file_path = arguments['config_file']
        self.base = BaseHandler()
        self.specification = self.valid_specification_dataset()
        self.writers = writers

<<<<<<< HEAD
    def get_valid_specification(self):
        config_reader = ConfigurationValidator(self.file_path)
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
=======
    def valid_specification_dataset(self):
        valid = self.base.valid_specification(self.file_path)
        return valid
>>>>>>> feature/dryrun

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
                yield key, file_format, file_path

    def generate_dataframe(self, specification: dict) -> DataFrame:
        size = specification['size']
        dataframe = self.base.generate_dataframe(specification, size)
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
