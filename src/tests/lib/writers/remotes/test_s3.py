import boto3

from moto import mock_s3

from src.lib.formatters.csv import CsvFormatter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401
import pandas as pd


class TestS3Writer(object):
    """Unit-test for S3Writer class"""

    def test_writting_csv_with_records(self,
                                       pandas_dataframe_with_data,
                                       specification_s3):
        with mock_s3():
            bucket = specification_s3['options']['bucket']
            key = specification_s3['options']['key']
            conn = boto3.resource('s3', region_name='us-east-1')
            conn.create_bucket(Bucket=bucket)

            formatter = CsvFormatter(specification={})
            writer = S3RemoteWriter(formatter=formatter,
                                    specification=specification_s3)
            writer.write(dataframe=pandas_dataframe_with_data)

            body = conn.Object(bucket, key).get()['Body']

            csv_reader = pd.read_csv(body).to_dict(orient="list")
            expected = pandas_dataframe_with_data.to_dict(orient="list")

            assert csv_reader == expected

    def test_writting_csv_without_records(self,
                                          pandas_dataframe_without_data,
                                          specification_s3):
        with mock_s3():
            bucket = specification_s3['options']['bucket']
            key = specification_s3['options']['key']
            conn = boto3.resource('s3', region_name='us-east-1')
            conn.create_bucket(Bucket=bucket)

            formatter = CsvFormatter(specification={})
            writer = S3RemoteWriter(formatter=formatter,
                                    specification=specification_s3)
            writer.write(dataframe=pandas_dataframe_without_data)

            object_ = conn.Object(bucket, key).get()

            assert object_['ContentLength'] == 0
