from src.lib.writers.remotes.gcs_presigned_url import GCSPresignedUrlRemoteWriter
from src.lib.formatters import formatters
from src.tests.lib.\
    writers.remotes.remotes_fixtures import (pandas_dataframe_with_data,
                                             test_file_path)
import pytest
import requests

spec_options = {
        "uri": "http://anyurihere"
    }


class TestGcsWriter:
    def test_write_dataframe_csv(self, mocker,
                                 pandas_dataframe_with_data,
                                 test_file_path):
        mock = mocker.patch.object(requests, 'put')
        mock.return_value = requests.codes.ok
        csv_formatter = formatters['csv']({"options": {"header": True}})
        gcs = GCSPresignedUrlRemoteWriter(formatter=csv_formatter,
                                          specification=spec_options)
        gcs.write(pandas_dataframe_with_data)

        assert True

    def test_write_dataframe_json(self, mocker,
                                  pandas_dataframe_with_data,
                                  test_file_path):
        json_formatter = formatters['json']({"options": {"orient": "records"}})
        gcs = GCSPresignedUrlRemoteWriter(formatter=json_formatter,
                                          specification=spec_options)

        with pytest.raises(requests.RequestException):
            gcs.write(pandas_dataframe_with_data)
