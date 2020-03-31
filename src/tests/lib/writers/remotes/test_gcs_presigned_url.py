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
            writer.write(dataframe=pandas_dataframe_without_data)
