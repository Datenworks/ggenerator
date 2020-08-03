from src.lib.writers.remotes.gcs_presigned_url \
    import GCSPresignedUrlRemoteWriter
from src.lib.formatters.csv import CsvFormatter
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401
import pytest
import requests


class TestGcsWriter:
    def test_writting_csv_with_records(self,
                                       mocker,
                                       specification_url_gcs,
                                       pandas_dataframe_with_data):

        mock = mocker.patch.object(requests, 'put')
        resp = requests.Response()
        resp.status_code = 200
        mock.return_value = resp

        formatter = CsvFormatter(specification={})
        writer = \
            GCSPresignedUrlRemoteWriter(formatter=formatter,
                                        specification=specification_url_gcs)
        writer.before_write()
        writer.write(dataframe=pandas_dataframe_with_data)
        mock.assert_called()

    def test_writting_csv_without_records(self,
                                          mocker,
                                          pandas_dataframe_without_data,
                                          specification_url_gcs):

        mock = mocker.patch.object(requests, 'put')
        resp = requests.Response()
        resp.status_code = 200
        mock.return_value = resp
        formatter = CsvFormatter(specification={})
        writer = \
            GCSPresignedUrlRemoteWriter(formatter=formatter,
                                        specification=specification_url_gcs)
        writer.before_write()
        writer.write(dataframe=pandas_dataframe_without_data)
        mock.assert_called()

    def test_writting_raised(self,
                             mocker,
                             pandas_dataframe_without_data,
                             specification_url_gcs):

        formatter = CsvFormatter(specification={})
        writer = \
            GCSPresignedUrlRemoteWriter(formatter=formatter,
                                        specification=specification_url_gcs)

        with pytest.raises(requests.RequestException):
            writer.before_write()
            writer.write(dataframe=pandas_dataframe_without_data)

    def test_without_url_and_valid_input(self,
                                         mocker,
                                         pandas_dataframe_without_data,
                                         gcs_without_url,
                                         specification_url_gcs):
        expected = specification_url_gcs['uri']
        response = requests.Response()
        response.status_code = 200
        response.url = expected

        mock_put = mocker.patch.object(requests, 'put')
        mock_put.return_value = response

        mock_input = mocker.patch('builtins.input')
        mock_input.return_value = expected

        formatter = CsvFormatter(specification={})
        writer = \
            GCSPresignedUrlRemoteWriter(formatter=formatter,
                                        specification=gcs_without_url)
        writer.before_write()
        signed_url = writer.write(dataframe=pandas_dataframe_without_data)

        mock_put.assert_called()

        assert signed_url == "gs://"
