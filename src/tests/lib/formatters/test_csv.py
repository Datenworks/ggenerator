from io import StringIO

from src.lib.formatters.csv import CsvFormatter
from src.tests.lib.formatters.fixtures import *  # noqa: F403, F401


class TestCsvFormatter(object):
    """Unit-test of CsvWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data):
        buffer = StringIO()
        csv_writer = CsvFormatter(specification={})
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) > 0

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data):
        buffer = StringIO()
        csv_writer = CsvFormatter(specification={})
        csv_writer.format(dataframe=pandas_dataframe_without_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) == 0
