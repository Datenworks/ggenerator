import requests

from io import StringIO
from pandas import DataFrame


class S3PresignedUrlRemoteWriter(object):
    key = 's3-url'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame):
        buffer = StringIO()
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=buffer)
        signed_url = self.specification['uri']
        requests.put(url=signed_url, data=buffer)
