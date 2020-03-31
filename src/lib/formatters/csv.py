import csv

from pandas import DataFrame


class CsvFormatter(object):
    """Class that receive pandas dataframe
    and write it down in CSV format
    """
    key = 'csv'

    def __init__(self, specification):
        self.default = {'index': False, 'sep': ','}
        self.specification = specification

    @staticmethod
    def rules():
        return {'required': {},
                'optional': {
                    'options.header': {'none': False, 'type': bool},
                    'options.sep': {'none': False, 'type': str},
                    'options.index': {'none': False, 'type': bool}
                }}

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
