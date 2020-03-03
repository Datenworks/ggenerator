import requests

from io import StringIO
from pandas import DataFrame


class GCSPresignedUrlRemoteWriter(object):
    key = 'gcs-url'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame):
        buffer = StringIO()
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=buffer)
        signed_url = self.specification['uri']
        self.__write(signed_url, buffer)
        return signed_url

    def __write(self, url, data):
        try:
            requests.put(url=url, data=data)
        except Exception as e:
            raise requests.RequestException("Can't send data to this given"
                                            "URI try to check if still valid",
                                            e)

    @staticmethod
    def is_valid_destination(**kwargs):
        return kwargs['uri'][:7] == 'http://'
