from src.lib.writers.csv import CsvWriter
from src.lib.writers.json import JsonWriter

writers = {'csv': CsvWriter, 'json': JsonWriter}


def valid_dataframe(dataframe):
    """Validates if dataframe contain records

    Parameters:
     - dataframe - pandas.DataFrame: dataframe containing the records
    """
    return dataframe.shape[0] > 0
