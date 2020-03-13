from pandas import DataFrame
import csv


class CsvFormatter(object):
    """Class that receive pandas dataframe
    and write it down in CSV format
    """
    key = 'csv'

    def __init__(self, specification):
        self.default = {'index': False, 'sep': ','}
        self.specification = specification

    def format(self, dataframe: DataFrame, path_or_buffer) -> None:
        """Format dataframe to csv.

        Parameters:
         - dataframe - pandas.DataFrame: dataframe containing the records.
        """
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        if dataframe.shape[0] > 0:
            return dataframe.to_csv(path_or_buf=path_or_buffer,
                                    quoting=csv.QUOTE_NONNUMERIC, **parameters)

    @staticmethod
    def check(*args, **kwargs):
        return True
