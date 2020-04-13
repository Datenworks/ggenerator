from io import StringIO
from pytest import raises

from src.lib.formatters.sql import SQLFormatter
from src.tests.lib.formatters.fixtures import *  # noqa: F403, F401


class TestSqlFormatter(object):
    """Unit-test of CsvWriter class"""

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

    def test_sql_script_is_append(self,
                                  pandas_dataframe_with_data):
        buffer = StringIO()
        csv_writer = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'mode': 'append',
                'schema': {
                    'Column': {
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
                    'Column': {
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
                    'Column': {
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

    def test_truncate(self, pandas_dataframe_with_data):
        buffer = StringIO()
        table_name = 'mytable'
        sql_writer = SQLFormatter(specification={
            'options': {
                'mode': 'truncate',
                'table_name': table_name,
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

        text = buffer.getvalue()
        assert isinstance(text, str) is True
        assert len(text) > 0
        assert f'TRUNCATE {table_name}' in text

    def test_replace(self, pandas_dataframe_with_data):
        buffer = StringIO()
        table_name = 'mytable'
        sql_writer = SQLFormatter(specification={
            'options': {
                'mode': 'replace',
                'table_name': table_name,
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

        text = buffer.getvalue()
        assert isinstance(text, str) is True
        assert len(text) > 0
        assert f'DROP TABLE IF EXISTS {table_name};' in text

    def test_invalid_mode(self, pandas_dataframe_with_data):
        buffer = StringIO()
        table_name = 'mytable'
        sql_writer = SQLFormatter(specification={
            'options': {
                'mode': 'invalid',
                'table_name': table_name,
                'batch_size': 2,
                'schema': {
                    'Column': {
                        'quoted': True
                    }
                }
            }
        })

        with raises(ValueError):
            sql_writer.format(dataframe=pandas_dataframe_with_data,
                              path_or_buffer=buffer)
