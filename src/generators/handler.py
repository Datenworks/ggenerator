from pandas import DataFrame, Series

from src.generators.datatypes import generators_map
from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset
from src.lib.writers import writers
from src.generators.basehandler import BaseHandler


class GeneratorsHandler(object):
    """GeneratorsHandler is responsible to integrate
    all the modules, serving like a facade to the user.
    """

    def __init__(self, arguments: dict):
        self.file_path = arguments['config_file']
        self.specification = self.valid_specification_dataset()
        self.writers = writers

    def valid_specification_dataset(self):
        base = BaseHandler()
        valid = base.valid_specification(self.file_path)
        return valid

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
        base = BaseHandler()
        dataframe = base.generate_dataframe(specification, size)
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
