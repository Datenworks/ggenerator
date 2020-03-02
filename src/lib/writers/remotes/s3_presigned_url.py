import requests

from io import StringIO
from pandas import DataFrame


class S3PresignedUrlRemoteWriter(object):
    key = 's3-url'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def check(specification):
        return "uri" in specification and \
            "fields" in specification

    def write(self, dataframe: DataFrame):
        fields = self.specification.get('fields')
        signed_url = self.specification['uri']

        buffer = StringIO()

        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=buffer)
        files = {'file': buffer.getvalue()}
        response = requests.post(signed_url,
                                 data=fields,
                                 files=files)
        response.raise_for_status()

        return signed_url
