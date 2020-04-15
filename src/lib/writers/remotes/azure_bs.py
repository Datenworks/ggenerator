from azure.storage.blob import BlobServiceClient
from os import getenv
from pandas import DataFrame
from io import StringIO


class AzureBSRemoteWriter(object):
    key = 'azure-bs'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification
        self.azure_bs = self.__azure_storage_client()

    def __azure_storage_client(self):
        connection_string = self.get_credentials()
        if not connection_string:
            raise Exception("AZURE_STORAGE_CONNECTION_STRING Not found. "
                            "Please set your environment variable "
                            "with your connection string")
        return BlobServiceClient\
            .from_connection_string(conn_str=connection_string)

    def get_credentials(self):
        return getenv("AZURE_STORAGE_CONNECTION_STRING", "")

    def write(self, dataframe: DataFrame) -> None:
        buffer = self.open_buffer()
        self.formatter.format(dataframe, buffer)

        options = self.specification['options']
        container = options['container']
        blob = options['blob']

        self.upload_blob(container=container, blob=blob, data=buffer)

        return f'{options["container"]}/{options["blob"]}'

    def open_buffer(self):
        buffer = StringIO()
        return buffer

    def upload_blob(self, container, blob, data: StringIO):
        self.azure_bs.get_blob_client(container=container,
                                      blob=blob)\
            .upload_blob(data.getvalue(), overwrite=True)

    @staticmethod
    def rules():
        return {'required': {'options.container': {'none': False, 'type': str},
                             'options.blob': {'none': False, 'type': str}},
                'optional': {}}
