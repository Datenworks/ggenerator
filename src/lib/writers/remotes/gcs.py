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

        try:
            file_buffer = self.gcstorage_fs.open(key, 'w')
            self.formatter.format(dataframe=dataframe,
                                  path_or_buffer=file_buffer)
        except gcsfs.utils.HttpError as e:
            raise Exception("Without permission", e)
        return key

    @staticmethod
    def is_valid_destination(**kwargs):
        options = kwargs.get('options')
        if options is None:
            raise EnvironmentError("Serializer GCS options not found.")
        if 'bucket' in options and 'key' in options and options is not None:
            return True
        return False
