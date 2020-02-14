from pandas import DataFrame

from src.lib.writers import writers


class GeneratorsHandler(object):
    def __init__(self, arguments: dict):
        self.file_path = arguments["config-file"]
        self.specification = self.__get_valid_specification()
        self.writers = writers

    def __get_valid_specification(self):
        pass

    def generate_dataframe(self) -> DataFrame:
        pass

    def write_dataframe(self, dataframe: DataFrame) -> None:
        file_format = self.specification["format"]["type"]
        file_path = self.specification["to"]["path"]

        writer = self.writers[file_format]()
        writer.write(dataframe=dataframe,
                     file_path=file_path,
                     **self.specification["format"])
