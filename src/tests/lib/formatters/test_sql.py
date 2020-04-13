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
                    'Column': {
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

    def test_invalid_quoted(self, schema_quoted_error):
        Sql_writer = SQLFormatter(specification={})
        msg_quoted_error = Sql_writer.rules.quoted_rule(schema_quoted_error)
        with pytest.raises(ValueError) as e:
            msg_quoted_error
        assert str(e.value) == " Schema fields required 'quoted'"

    def test_invalid_sqltype(self, schema_sqltype_error):
        Sql_writer = SQLFormatter(specification={})
        msg_sqltype_error = Sql_writer.rules.quoted_rule(schema_sqltype_error)
        with pytest.raises(ValueError) as e:
            msg_sqltype_error
        assert str(e.value) == \
            "The Mode replace needs'sqltype' in Schema fields"
