import json
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
        options = specification.get('options')
        if options is not None:
            return options

        return 'path' in options

    def write(self, dataframe: DataFrame):
        options = self.specification['options']
        file_path = options['path']

        with open(file_path, 'r') as file:
            singed_post = json.loads(file.read())

        signed_url = singed_post.get('url')
        fields = singed_post.get('fields')

        buffer = StringIO()
        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=buffer)

        files = {'file': buffer.getvalue()}
        response = requests.post(signed_url,
                                 data=fields,
                                 files=files)
        response.raise_for_status()

        return signed_url
