from pandas import DataFrame


class S3RemoteWriter(object):
    key = 's3'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame) -> None:
        options = self.specification['options']
        key = f's3://{options["bucket"]}/{options["key"]}'
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=key)

    @staticmethod
    def is_valid_destination(**kwargs):
        if kwargs['bucket'] and kwargs['key']:
            return True
        return False
