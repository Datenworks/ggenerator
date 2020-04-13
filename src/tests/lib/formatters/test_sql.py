from src.lib.formatters.sql import SQLFormatter
from src.tests.lib.formatters.fixtures import *  # noqa: F403, F401
import pytest
from io import StringIO


class TestSqlFormatter(object):
    """Unit-test of CsvWriter class"""

    def test_writting_dataframe_with_records(self,
                                             pandas_dataframe_with_data):
        buffer = StringIO()
        csv_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                }
            }
        })
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) > 0

    def test_sql_script_is_append(self,
                                  pandas_dataframe_with_data):
        buffer = StringIO()
        csv_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'mode': 'append',
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                }
            }
        })
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert "INSERT INTO".lower() in buffer.getvalue().lower()

    def test_sql_script_contain_dataframe_columns(self,
                                                  pandas_dataframe_with_data):
        buffer = StringIO()
        csv_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                }
            }
        })
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        for column in pandas_dataframe_with_data:
            assert column.lower() in buffer.getvalue().lower()

    def test_sql_script_contain_dataframe_rows(self,
                                               pandas_dataframe_with_data):
        buffer = StringIO()
        csv_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                }
            }
        })
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        for index, row in pandas_dataframe_with_data.iterrows():
            for column in pandas_dataframe_with_data.columns:
                assert row[column].lower() in buffer.getvalue().lower()

    def test_sql_script_contain_rows_and_index(self,
                                               pandas_dataframe_with_data):
        buffer = StringIO()
        index_flag = True
        index_label = 'myindexlabel'
        csv_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'index': index_flag,
                'index_label': index_label,
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                }
            }
        })
        csv_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert index_label in buffer.getvalue().lower()
        for index, row in pandas_dataframe_with_data.iterrows():
            for column in pandas_dataframe_with_data.columns:
                assert row[column].lower() in buffer.getvalue().lower()
                assert str(index) in buffer.getvalue().lower()

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
