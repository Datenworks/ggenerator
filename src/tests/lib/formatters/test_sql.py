from io import StringIO

from src.lib.formatters.sql import SQLFormatter
from src.tests.lib.formatters.fixtures import *  # noqa: F403, F401


class TestSqlFormatter(object):
    """Unit-test of SQLWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data):
        buffer = StringIO()
        sql_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'schema': {
                    'Column': {
                        'quoted': True
                    }
                }
            }
        })
        sql_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) > 0

    def test_writting_dataframe_without_records(self,
                                                pandas_dataframe_without_data):
        buffer = StringIO()
        sql_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'schema': {
                    'Column': {
                        'quoted': True
                    }
                }
            }
        })
        sql_writer.format(dataframe=pandas_dataframe_without_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) == 0

    def test_writing_sql_append_mode(
                                    self,
                                    pandas_dataframe_with_data,
                                    fixture_spec_default):
        buffer = StringIO()
        sql_writer = SQLFormatter(fixture_spec_default)
        sql_writer.format(pandas_dataframe_with_data, buffer)

        assert isinstance(buffer.getvalue(), str) is True
        #  assert len(buffer.getvalue()) == 0

    def test_writing_sql_replace_mode(
                                    self,
                                    replace_dataframe,
                                    fixture_spec_replace):
        buffer = StringIO()
        sql_writer = SQLFormatter(fixture_spec_replace)
        sql_writer.format(replace_dataframe, buffer)

        assert isinstance(buffer.getvalue(), str) is True
        #  assert len(buffer.getvalue()) == 0
