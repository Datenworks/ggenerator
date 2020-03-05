from pandas import DataFrame

from tabulate import tabulate
from src.generators.basehandler import BaseHandler


class DryRunHandler(object):
    """DryRunHandler is responsible to give
    a dataframe preview.
    """
    def __init__(self, arguments: dict):
        self.file_path = arguments['config_file']
        self.base = BaseHandler()
        self.specification = self.valid_specification_dryrun()

    def valid_specification_dryrun(self):
        valid = self.base.valid_specification(self.file_path)
        return valid

    def generate(self):
        datasets = self.specification.get('datasets')
        for key in datasets.keys():
            dataset = datasets[key]
            dataset_fields = dataset['fields']
            dataframe = self.generate_dryrun(dataset)
            dryrun = self.print_dryrun(dataframe, key, dataset_fields)
        return dryrun

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
        print(tabulate(
            dataframe, tablefmt="fancy_grid",
            headers=dataframe.columns))

    def generate_dryrun(self, specification: dict) -> DataFrame:
        dataframe = self.base.generate_dataframe(specification, 10)
        return dataframe
