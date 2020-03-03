from s3fs.core import S3FileSystem
from pandas import DataFrame


class S3RemoteWriter(object):
    key = 's3'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def check(specification):
        options = specification.get("options")
        if options is None:
            return False

        return "bucket" in options and \
            "key" in options

    def write(self, dataframe: DataFrame) -> None:
        s3 = S3FileSystem(anon=False)
        options = self.specification['options']
        key = f's3://{options["bucket"]}/{options["key"]}'
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=s3.open(key, mode='w'))
        return key
