from pandas import DataFrame

from src.lib.writers import valid_dataframe


class JsonWriter(object):
    """Class that receive pandas dataframe
    and write it down in Json format
    """

    def __init__(self):
        pass

    def write(self, dataframe: DataFrame, file_path: str, **kwargs) -> None:
        """Write all dataframe on a .json file.

        Keyword arguments:
         - dataframe - pandas.Dataframe: dataframe containing the records
         - file_path - str: path of the file to be written
         - **kwargs - additional arguments for "to_json" pandas method
        """
        if valid_dataframe(dataframe=dataframe) is True:
            dataframe.to_json(file_path, **kwargs)