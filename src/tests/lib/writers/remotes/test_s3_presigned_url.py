import json
import requests

from mock import mock_open, patch

from src.lib.formatters.csv import CsvFormatter
from src.lib.writers.remotes.s3_presigned_url import S3PresignedUrlRemoteWriter
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401


class TestS3PresignedUrlRemoteWriter(object):
    """Unit-test for S3PresignedUrlRemoteWriter class"""

    def test_writting_csv_with_records(self,
                                       mocker,
                                       specification_url,
                                       pandas_dataframe_with_data,
                                       signed_post_file):
        mock_post = mocker.patch.object(requests, 'post')
        mock_post.return_value.raise_for_status = lambda: None

        with patch('builtins.open',
                   mock_open(read_data=signed_post_file)) as mock_file:
            formatter = CsvFormatter(specification={})
            writer = S3PresignedUrlRemoteWriter(
                formatter=formatter,
                specification=specification_url
            )
            signed_url = writer.write(dataframe=pandas_dataframe_with_data)

            mock_post.assert_called()
            mock_file.assert_called()

            expected = json.loads(signed_post_file)['url']

            assert signed_url == expected

    def test_writting_csv_without_records(self,
                                          mocker,
                                          pandas_dataframe_without_data,
                                          specification_url,
                                          signed_post_file):
        mock_post = mocker.patch.object(requests, 'post')
        mock_post.return_value.raise_for_status = lambda: None

        with patch('builtins.open',
                   mock_open(read_data=signed_post_file)) as mock_file:
            formatter = CsvFormatter(specification={})
            writer = S3PresignedUrlRemoteWriter(
                formatter=formatter,
                specification=specification_url
            )
            signed_url = writer.write(dataframe=pandas_dataframe_without_data)

            mock_post.assert_called()
            mock_file.assert_called()

            expected = json.loads(signed_post_file)['url']

            assert signed_url == expected
