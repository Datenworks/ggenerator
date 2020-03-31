from csv import reader
from os import remove
from os.path import exists, isfile

from src.lib.formatters.csv import CsvFormatter
from src.lib.writers.file import FileWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401


class TestFileWriter(object):
    """Unit-test for FileWriter class"""

    def test_writting_csv_with_records(self,
                                       pandas_dataframe_with_data,
                                       specification):
        formatter = CsvFormatter(specification={})
        writer = FileWriter(formatter=formatter, specification=specification)
        writer.write(dataframe=pandas_dataframe_with_data)

        assert exists(specification['uri']) is True
        assert isfile(specification['uri']) is True

        with open(specification['uri']) as csv_file:
            csv_reader = reader(csv_file, delimiter=',')
            csv_reader = [x for x in csv_reader]
            headers = csv_reader[0]
            rows = csv_reader[1:len(csv_reader)]
            csv_reader = {headers[index]: [row[index]
                                           for row in rows]
                          for index in range(0, len(headers))}
            expected = pandas_dataframe_with_data.to_dict(orient="list")

            assert csv_reader == expected

        remove(specification['uri'])
        assert exists(specification['uri']) is False

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data,
                                                specification):
        formatter = CsvFormatter(specification={})
        writer = FileWriter(formatter=formatter, specification=specification)
        writer.write(dataframe=pandas_dataframe_without_data)

        assert exists(specification['uri']) is False
        assert isfile(specification['uri']) is False
