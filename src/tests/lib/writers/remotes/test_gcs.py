from src.lib.writers.remotes.gcs import GCSRemoteWriter
from src.lib.formatters import formatters
from src.tests.lib.\
    writers.remotes.remotes_fixtures import (pandas_dataframe_with_data,
                                             test_file_path)
from csv import reader
import gcsfs
from io import StringIO
spec_options = {
        "options": {
            "bucket": "ggnerator",
            "key": "path/to/file.csv"
        }
    }


class TestGcsWriter:
    def test_write_dataframe_csv(self, mocker,
                                 pandas_dataframe_with_data,
                                 test_file_path):
        buffer = StringIO()
        mock = mocker.patch.object(gcsfs, 'GCSFileSystem')
        mock.return_value.open.return_value = buffer

        csv_formatter = formatters['csv']({"options": {"header": True}})
        gcs = GCSRemoteWriter(formatter=csv_formatter,
                              specification=spec_options)
        gcs.write(pandas_dataframe_with_data)
        expected = pandas_dataframe_with_data.to_dict(orient="list")

        buffer.seek(0)
        csv_reader = reader(buffer.readlines(), delimiter=',')
        csv_reader = [x for x in csv_reader]
        headers = csv_reader[0]
        rows = csv_reader[1:len(csv_reader)]
        csv_reader = {headers[index]: [row[index]
                      for row in rows]
                      for index in range(0, len(headers))}
        assert csv_reader == expected

    def test_write_dataframe_json(self, mocker,
                                  pandas_dataframe_with_data,
                                  test_file_path):
        buffer = StringIO()
        mock = mocker.patch.object(gcsfs, 'GCSFileSystem')
        mock.return_value.open.return_value = buffer

        json_formatter = formatters['json']({"options": {"orient": "records"}})
        gcs = GCSRemoteWriter(formatter=json_formatter,
                              specification=spec_options)
        gcs.write(pandas_dataframe_with_data)
        expected = pandas_dataframe_with_data.to_json(orient="records")

        buffer.seek(0)
        assert buffer.read() == expected
