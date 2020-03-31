from pandas import DataFrame
import gcsfs


class GCSRemoteWriter(object):
    key = 'gcs'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification
        self.gcstorage_fs = gcsfs.GCSFileSystem(token='google_default')

    def write(self, dataframe: DataFrame) -> None:
        if self.gcstorage_fs.token is None:
            raise Exception("Without permission, please login")
        options = self.specification['options']
        key = f'gs://{options["bucket"]}/{options["key"]}'
        file_buffer = self.gcstorage_fs.open(key, 'w')
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=file_buffer)
        return key

    @staticmethod
    def rules():
        return {'required': {'options.bucket': {'none': False, 'type': str},
                             'options.key': {'none': False, 'type': str}},
                'optional': {}}
