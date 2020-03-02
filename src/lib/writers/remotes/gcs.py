from pandas import DataFrame
import gcsfs


class GCSRemoteWriter(object):
    key = 'gcs'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification
        self.gcstorage_fs = gcsfs.GCSFileSystem()

    def write(self, dataframe: DataFrame) -> None:
        options = self.specification['options']
        key = f'gs://{options["bucket"]}/{options["key"]}'
        file_buffer = self.gcstorage_fs.open(key, 'w')
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=file_buffer)

    @staticmethod
    def is_valid_destination(**kwargs):
        if kwargs['bucket'] and kwargs['key']:
            return True
        return False
