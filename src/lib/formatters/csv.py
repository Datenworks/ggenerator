import csv

from datetime import datetime
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

        date_format = options.get('date_format')
        if date_format == 'epoch':
            parameters.pop('date_format')
            epoch = datetime(1970, 1, 1)
            for column in dataframe.columns:
                if dataframe[column].dtype == 'datetime64[ns]':
                    dataframe[column] = \
                        dataframe[column].apply(lambda x: int((x - epoch)
                                                .total_seconds()))
        elif date_format == 'iso':
            parameters.update({'date_format': '%Y-%m-%dT%H:%M:%SZ'})

        if dataframe.shape[0] > 0:
            return dataframe.to_csv(path_or_buf=path_or_buffer,
                                    quoting=csv.QUOTE_NONNUMERIC, **parameters)
