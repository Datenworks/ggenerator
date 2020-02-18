from pandas import DataFrame

from src.lib.writers import valid_dataframe


class CsvWriter(object):
    """Class that receive pandas dataframe
    and write it down in CSV format
    """

    def __init__(self):
        pass

    def write(self, dataframe: DataFrame, file_path: str, **kwargs) -> None:
        """Write all dataframe on a .csv file.

        Parameters:
         - dataframe - pandas.DataFrame: dataframe containing the records.
         - file_path - str: path of the file to be written.
         - **kwargs - additional arguments for "to_csv" pandas method.
        """
        if valid_dataframe(dataframe=dataframe) is True:
            dataframe.to_csv(file_path, **kwargs)
