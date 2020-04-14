import json
import requests
import os

from io import StringIO
from pandas import DataFrame


class S3PresignedUrlRemoteWriter(object):
    key = 's3-url'
    file_path = None

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def before_write(self):
        options = self.specification.get('options')

        if options is None:
            file_path = input("Enter the signed url json file path: ")
            if os.path.isfile(file_path) is False:
                raise ValueError('File not found')
            self.file_path = file_path

    def write(self, dataframe: DataFrame):
        with open(self.file_path, 'r') as file:
            singed_post = json.loads(file.read())

        signed_url = singed_post.get('url')
        fields = singed_post.get('fields')

        buffer = StringIO()
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=buffer)

        files = {'file': buffer.getvalue()}

        try:
            response = requests.post(signed_url,
                                     data=fields,
                                     files=files)
            response.raise_for_status()
        except Exception as e:
            raise requests.RequestException("Can't send data to this given"
                                            "URI try to check if still valid",
                                            e)
        return signed_url

    @staticmethod
    def rules():
        return {'required': {},
                'optional': {'options.path': {'none': False, 'type': str}}}
