from pandas import DataFrame, Series

from src.generators.datatypes import generators_map
from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset
from tabulate import tabulate
from src.generators.basehandler import BaseHandler


class DryRunHandler(object):
    """GeneratorsHandler is responsible to integrate
    all the modules, serving like a facade to the user.
    """
    def __init__(self, arguments: dict):
        self.file_path = arguments['config_file']
        self.specification = self.valid_specification_dryrun()

    def valid_specification_dryrun(self):
        base = BaseHandler()
        valid = base.valid_specification(self.file_path)
        return valid

    def generate(self):
        datasets = self.specification.get('datasets')
        for key in datasets.keys():
            dataset = datasets[key]
            dataset_fields = dataset['fields']
            dataframe = self.generate_dryrun(dataset)
            self.print_dryrun(dataframe, key, dataset_fields)

    def print_dryrun(self, dataframe, key, dataset_fields):
        print("Dataset: ", key)
        self.__print_fields(dataset_fields)
        print("-------------------")
        print("First 10 rows: \n")
        self.__print_dataframe(dataframe)
        print("-------------------")

    def __print_fields(self, dataset_fields):
        for field in dataset_fields:
            print("   ", field['name'], ":", field['type'])

    def __print_dataframe(self, dataframe):
        print(tabulate(dataframe, tablefmt="fancy_grid",
                                  headers = dataframe.columns))

    def generate_dryrun(self, specification: dict) -> DataFrame:
        base = BaseHandler()
        size = 10
        dataframe = base.generate_dataframe(specification, size)
        return dataframe
