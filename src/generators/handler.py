from pandas import DataFrame, Series

from src.generators.datatypes import generators_map
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
        pass

    def generate_dataframe(self) -> DataFrame:
        size = self.specification['size']
        fields = self.specification['fields']

        dataframe = DataFrame()
        for field in fields:
            field_name = field['name']
            field_type = field['type']
            field_arguments = field['generator']

            generator_class = generators_map[field_type]
            generator = generator_class(**field_arguments)

            series = Series(generator.generate_records(size))

            dataframe[field_name] = series.values

        return dataframe

    def write_dataframe(self, dataframe: DataFrame) -> None:
        file_format = self.specification['format']['type']
        file_path = self.specification['to']['path']

        writer = self.writers[file_format]()
        writer.write(dataframe=dataframe,
                     file_path=file_path,
                     **self.specification['format'])
