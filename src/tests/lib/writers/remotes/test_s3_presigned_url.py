import requests

from src.lib.formatters.csv import CsvFormatter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401


class TestS3PresignedUrlRemoteWriter(object):
    """Unit-test for S3PresignedUrlRemoteWriter class"""

    def test_writting_csv_with_records(self,
                                       mocker,
                                       specification_url,
                                       pandas_dataframe_with_data):
        mock = mocker.patch.object(requests, 'put')
        mock.return_value = {}
        formatter = CsvFormatter(specification={})
        writer = S3PresignedUrlRemoteWriter(formatter=formatter,
                                            specification=specification_url)
        writer.write(dataframe=pandas_dataframe_with_data)

        mock.assert_called()

    def test_writting_csv_without_records(self,
                                          mocker,
                                          pandas_dataframe_without_data,
                                          specification_url):
        mock = mocker.patch.object(requests, 'put')
        mock.return_value = {}
        formatter = CsvFormatter(specification={})
        writer = S3PresignedUrlRemoteWriter(formatter=formatter,
                                            specification=specification_url)
        writer.write(dataframe=pandas_dataframe_without_data)

        mock.assert_called()
