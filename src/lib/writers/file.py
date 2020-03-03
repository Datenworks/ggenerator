from pandas import DataFrame


class FileWriter(object):
    """Class that receive pandas dataframe
    and write it down in Json format
    """
    key = 'file'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def check(specification):
        return "uri" in specification

    def write(self, dataframe: DataFrame) -> None:
        """Write all dataframe on a .json file.

        Keyword arguments:
         - dataframe - pandas.Dataframe: dataframe containing the records
        """
        file_path = self.specification['uri']
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=file_path)
        return file_path
