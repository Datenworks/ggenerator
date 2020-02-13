import os.path

from csv import reader
# from os import remove
# from os.path import exists, isfile

from src.lib.writers.csv import CsvWriter
from tests.lib.writers.writers_fixtures import pandas_dataframe_with_data, \
    pandas_dataframe_without_data, test_file_path


class TestCsvWriter:
    """Unit-test of CsvWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data,
                                             test_file_path):
        csv_writer = CsvWriter()
        csv_writer.write(dataframe=pandas_dataframe_with_data,
                         file_path=test_file_path,
                         index=False)
        assert os.path.exists(test_file_path) is True
        assert os.path.isfile(test_file_path) is True

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

        os.remove(test_file_path)
        assert os.path.exists(test_file_path) is False

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data,
                                                test_file_path):
        csv_writer = CsvWriter()
        csv_writer.write(dataframe=pandas_dataframe_without_data,
                         file_path=test_file_path,
                         index=False)
        assert os.path.exists(test_file_path) is False
        assert os.path.isfile(test_file_path) is False
