from src.lib.writers.remotes.azure_bs import AzureBSRemoteWriter
from src.lib.formatters import formatters
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401
import pytest
from io import StringIO
from csv import reader
from azure.storage.blob import BlobServiceClient


class TestAzureBSWriter(object):
    def test_azure_without_connection_string(self,
                                             mocker,
                                             specification_azure_bs):
        csv_formatter = formatters['csv']({"options": {"header": True}})
        mock = mocker.patch.object(AzureBSRemoteWriter, 'get_credentials')
        mock.return_value = ""

        with pytest.raises(Exception):
            AzureBSRemoteWriter(formatter=csv_formatter,
                                specification=specification_azure_bs)

    def test_write_dataframe_csv(self, mocker,
                                 pandas_dataframe_with_data,
                                 specification_azure_bs):
        mock = mocker.patch.object(BlobServiceClient, 'from_connection_string')
        mock.return_value = None

        mock_credential = mocker.patch.object(
            AzureBSRemoteWriter, 'get_credentials')
        mock_credential.return_value = "MyCredential"

        buffer = StringIO()
        mock_buffer = mocker.patch.object(AzureBSRemoteWriter, 'open_buffer')
        mock_buffer.return_value = buffer

        mock_upload = mocker.patch.object(
            AzureBSRemoteWriter, 'upload_blob')
        mock_upload.return_value = None

        csv_formatter = formatters['csv']({"options": {"header": True}})
        azure_bs = AzureBSRemoteWriter(formatter=csv_formatter,
                                       specification=specification_azure_bs)
        azure_bs.write(pandas_dataframe_with_data)
        expected = pandas_dataframe_with_data.to_dict(orient="list")

        buffer.seek(0)
        csv_reader = reader(buffer.readlines(), delimiter=',')
        csv_reader = [x for x in csv_reader]
        headers = csv_reader[0]
        rows = csv_reader[1:len(csv_reader)]
        csv_reader = {headers[index]: [row[index]
                                       for row in rows]
                      for index in range(0, len(headers))}

        assert csv_reader == expected

    def test_write_dataframe_json(self, mocker,
                                  pandas_dataframe_with_data,
                                  specification_azure_bs):
        mock = mocker.patch.object(BlobServiceClient, 'from_connection_string')
        mock.return_value.open.return_value = None

        mock_credential = mocker.patch.object(
            AzureBSRemoteWriter, 'get_credentials')
        mock_credential.return_value = "MyCredential"

        buffer = StringIO()
        mock_buffer = mocker.patch.object(AzureBSRemoteWriter, 'open_buffer')
        mock_buffer.return_value = buffer

        mock_upload = mocker.patch.object(
            AzureBSRemoteWriter, 'upload_blob')
        mock_upload.return_value = None

        json_formatter = formatters['json-array'](
            {"options": {"orient": "records"}})

        azure_bs = AzureBSRemoteWriter(formatter=json_formatter,
                                       specification=specification_azure_bs)
        azure_bs.write(pandas_dataframe_with_data)
        expected = pandas_dataframe_with_data.to_json(orient="records")

        assert buffer.getvalue() == expected
