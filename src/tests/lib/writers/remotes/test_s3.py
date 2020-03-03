import boto3

from moto import mock_s3

from src.lib.formatters.csv import CsvFormatter
from src.lib.writers.remotes.s3 import S3RemoteWriter
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401


class TestS3Writer(object):
    """Unit-test for S3Writer class"""

    def test_writting_csv_with_records(self,
                                       pandas_dataframe_with_data,
                                       specification):
        with mock_s3():
            bucket = specification['options']['bucket']
            key = specification['options']['key']
            conn = boto3.resource('s3', region_name='us-east-1')
            conn.create_bucket(Bucket=bucket)

            formatter = CsvFormatter(specification={})
            writer = S3RemoteWriter(formatter=formatter,
                                    specification=specification)
            writer.write(dataframe=pandas_dataframe_with_data)

            body = conn.Object(bucket, key).get()['Body'].read().decode()

            body = body.split('\n')
            body = [x.split(',') for x in body]
            headers = body[0]
            rows = body[1:len(body) - 1]
            csv_reader = {headers[index]: [row[index]
                                           for row in rows]
                          for index in range(0, len(headers))}
            expected = pandas_dataframe_with_data.to_dict(orient="list")

            assert csv_reader == expected

    def test_writting_csv_without_records(self,
                                          pandas_dataframe_without_data,
                                          specification):
        with mock_s3():
            bucket = specification['options']['bucket']
            key = specification['options']['key']
            conn = boto3.resource('s3', region_name='us-east-1')
            conn.create_bucket(Bucket=bucket)

            formatter = CsvFormatter(specification={})
            writer = S3RemoteWriter(formatter=formatter,
                                    specification=specification)
            writer.write(dataframe=pandas_dataframe_without_data)

            object_ = conn.Object(bucket, key).get()

            assert object_['ContentLength'] == 0
