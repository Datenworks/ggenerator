from pandas import DataFrame


class GCSRemoteWriter(object):
    key = 'gcs'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame) -> None:
        options = self.specification['options']
        key = f'gs://{options["bucket"]}/{options["key"]}'
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=key)
