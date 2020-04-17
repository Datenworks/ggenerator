import requests

from io import StringIO
from pandas import DataFrame
from urllib.parse import urlparse


class GCSPresignedUrlRemoteWriter(object):
    key = 'gcs-url'
    signed_url = None

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def before_write(self):
        self.signed_url = self.specification.get('uri')

        if not self.signed_url:
            self.signed_url = input("Enter the signed url: ")

    def write(self, dataframe: DataFrame):
        buffer = StringIO()

        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=buffer)

        try:
            response = requests.put(self.signed_url,
                                    data=buffer.getvalue())
            response.raise_for_status()
        except Exception as e:
            raise requests.RequestException("Can't send data to this given"
                                            "URI try to check if still valid",
                                            e)
        return self.__get_file_path_from_resp(response)

    def __get_file_path_from_resp(self, resp):
        return f"gs://{urlparse(resp.url).path}"

    @staticmethod
    def rules():
        return {'required': {},
                'optional': {'uri': {'none': False, 'type': str}}}
