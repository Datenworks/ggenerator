from os import remove
from os.path import exists, isfile

from src.lib.formatters.json import JsonFormatter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401


class TestJsonWriter:
    """Unit-test of JsonWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data,
                                             specification):
        test_file_path = specification['uri']
        json_writer = JsonFormatter()
        json_writer.format(dataframe=pandas_dataframe_with_data,
                           path_or_buffer=test_file_path)
        assert exists(test_file_path) is True
        assert isfile(test_file_path) is True

        with open(test_file_path) as json_file:
            expected = pandas_dataframe_with_data.to_json(orient="records")

            assert json_file.read() == expected

        remove(test_file_path)
        assert exists(test_file_path) is False

    def test_writting_dataframe_with_records_orient_columns(
            self,
            pandas_dataframe_with_data,
            specification):
        test_file_path = specification['uri']
        json_writer = JsonFormatter(specification={
            "options":
                {"orient": "columns"}
            }
        )
        json_writer.format(dataframe=pandas_dataframe_with_data,
                           path_or_buffer=test_file_path)
        assert exists(test_file_path) is True
        assert isfile(test_file_path) is True

        with open(test_file_path) as json_file:
            expected = pandas_dataframe_with_data.to_json(orient="columns")

            assert json_file.read() == expected

        remove(test_file_path)
        assert exists(test_file_path) is False

    def test_writting_dataframe_with_records_orient_records(
            self,
            pandas_dataframe_with_data,
            specification):
        test_file_path = specification['uri']
        json_writer = JsonFormatter(specification={
            "options":
                {"orient": "records"}
            }
        )
        json_writer.format(dataframe=pandas_dataframe_with_data,
                           path_or_buffer=test_file_path)
        assert exists(test_file_path) is True
        assert isfile(test_file_path) is True

        with open(test_file_path) as json_file:
            expected = pandas_dataframe_with_data.to_json(orient="records")

            assert json_file.read() == expected

        remove(test_file_path)
        assert exists(test_file_path) is False

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data,
                                                specification):
        test_file_path = specification['uri']
        json_writer = JsonFormatter()
        json_writer.format(dataframe=pandas_dataframe_without_data,
                           path_or_buffer=test_file_path)
        assert exists(test_file_path) is False
        assert isfile(test_file_path) is False
