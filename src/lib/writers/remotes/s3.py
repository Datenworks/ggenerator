from s3fs.core import S3FileSystem
from pandas import DataFrame


class S3RemoteWriter(object):
    key = 's3'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame) -> None:
        s3 = S3FileSystem(anon=False)
        options = self.specification['options']
        key = f's3://{options["bucket"]}/{options["key"]}'
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=s3.open(key, mode='w'))

        return key

    @staticmethod
    def is_valid_destination(**kwargs):
        options = kwargs.get('options')
        if options is None:
            raise ValueError(
                            "Options not in specifications, please add it")
        elif 'bucket' not in options or options['bucket'] == "":
            raise ValueError("Please, add your bucket name")
        elif 'key' not in options or options['key'] == "":
            raise ValueError("Please, add your key/path")
        elif options and 'bucket' in options and 'key' in options:
            return True
