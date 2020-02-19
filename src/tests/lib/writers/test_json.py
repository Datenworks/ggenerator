from os import remove
from os.path import exists, isfile

from src.lib.writers.json import JsonWriter
from src.tests.lib.writers.writers_fixtures import pandas_dataframe_with_data, \
    pandas_dataframe_without_data, test_file_path


class TestJsonWriter:
    """Unit-test of JsonWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data,
                                             test_file_path):
        json_writer = JsonWriter()
        json_writer.write(dataframe=pandas_dataframe_with_data,
                          file_path=test_file_path)
        assert exists(test_file_path) is True
        assert isfile(test_file_path) is True

        with open(test_file_path) as json_file:
            expected = pandas_dataframe_with_data.to_json(orient="columns")

            assert json_file.read() == expected

        remove(test_file_path)
        assert exists(test_file_path) is False

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data,
                                                test_file_path):
        json_writer = JsonWriter()
        json_writer.write(dataframe=pandas_dataframe_without_data,
                          file_path=test_file_path)
        assert exists(test_file_path) is False
        assert isfile(test_file_path) is False
