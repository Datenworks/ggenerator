from csv import reader
from os import remove
from os.path import exists, isfile

from src.lib.formatters.csv import CsvFormatter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401


class TestCsvWriter:
    """Unit-test of CsvWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data,
                                             specification):
        test_file_path = specification['uri']
        csv_writer = CsvFormatter(specification={"options": {"index": False}})
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=test_file_path)
        assert exists(test_file_path) is True
        assert isfile(test_file_path) is True

        with open(test_file_path) as csv_file:
            csv_reader = reader(csv_file, delimiter=',')
            csv_reader = [x for x in csv_reader]
            headers = csv_reader[0]
            rows = csv_reader[1:len(csv_reader)]
            csv_reader = {headers[index]: [row[index]
                                           for row in rows]
                          for index in range(0, len(headers))}
            expected = pandas_dataframe_with_data.to_dict(orient="list")

            assert csv_reader == expected

        remove(test_file_path)
        assert exists(test_file_path) is False

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data,
                                                specification):
        test_file_path = specification['uri']
        csv_writer = CsvFormatter(specification={"options": {"index": False}})
        csv_writer.format(dataframe=pandas_dataframe_without_data,
                          path_or_buffer=test_file_path)
        assert exists(test_file_path) is False
        assert isfile(test_file_path) is False
