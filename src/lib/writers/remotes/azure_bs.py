from azure.storage.blob import BlobServiceClient
from os import getenv
from pandas import DataFrame


class AzureBlobStorage(object):
    key = 'azure-bs'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification
        self.azure_bs = self.__azure_storage_client()

    def __azure_storage_client(self):
        connection_string = getenv("AZURE_STORAGE_CONNECTION_STRING", "")
        if not connection_string:
            raise Exception("AZURE_STORAGE_CONNECTION_STRING Not found."
                            "Please set your environment variable."
                            "with your connection string")
        return BlobServiceClient\
            .from_connection_string(conn_str=connection_string)

    def write(self, dataframe: DataFrame) -> None:
        self.azure_bs.get_blob_client(container='<CONTAINER_NAME>',
                                      blob='<BLOB_NAME>')\
                     .upload_blob()
        pass

    @staticmethod
    def rules():
        return {'required': {'options.container': {'none': False, 'type': str},
                             'options.blob': {'none': False, 'type': str}},
                'optional': {}}
