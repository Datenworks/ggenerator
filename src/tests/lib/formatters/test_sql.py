from pytest import raises
from src.lib.formatters.sql import SQLFormatter
from src.tests.lib.formatters.fixtures import *  # noqa: F403, F401
from io import StringIO


class TestSqlFormatter(object):
    """Unit-test of SQLWriter class"""

    def test_writting_dataframe_with_records(self,
                                             sql_specification_format,
                                             pandas_dataframe_with_data):
        buffer = StringIO()
        sql_writer = SQLFormatter(
            specification=sql_specification_format('mytable', mode='append'))
        sql_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) > 0

    def test_sql_script_is_append(self,
                                  sql_specification_format,
                                  pandas_dataframe_with_data):
        buffer = StringIO()
        sql_writer = SQLFormatter(
            specification=sql_specification_format('mytable', mode='append'))
        sql_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        assert "INSERT INTO".lower() in buffer.getvalue().lower()

    def test_sql_script_contain_dataframe_columns(self,
                                                  sql_specification_format,
                                                  pandas_dataframe_with_data):
        buffer = StringIO()
        sql_writer = SQLFormatter(
            specification=sql_specification_format('mytable', mode='append'))
        sql_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        for column in pandas_dataframe_with_data:
            assert column.lower() in buffer.getvalue().lower()

    def test_sql_script_contain_dataframe_rows(self,
                                               sql_specification_format,
                                               pandas_dataframe_with_data):
        buffer = StringIO()
        sql_writer = SQLFormatter(
            specification=sql_specification_format('mytable', mode='append'))
        sql_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        for index, row in pandas_dataframe_with_data.iterrows():
            for column in pandas_dataframe_with_data.columns:
                assert row[column].lower() in buffer.getvalue().lower()

    def test_sql_script_contain_rows_and_index(self,
                                               sql_specification_format,
                                               pandas_dataframe_with_data):
        buffer = StringIO()
        index_flag = True
        index_label = 'myindexlabel'
        csv_writer = SQLFormatter(
            specification=sql_specification_format('mytable',
                                                   index=index_flag,
                                                   index_label=index_label,
                                                   mode='append'))
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
                'mode': 'append',
                'schema': {}
            }
        })
        sql_writer.format(dataframe=pandas_dataframe_without_data,
                          path_or_buffer=buffer)

        assert isinstance(buffer.getvalue(), str) is True
        assert len(buffer.getvalue()) == 0

    def test_truncate(self, sql_specification_format,
                      pandas_dataframe_with_data):
        buffer = StringIO()
        table_name = 'mytable'
        sql_writer = SQLFormatter(
            specification=sql_specification_format('mytable', mode='truncate'))
        sql_writer.format(dataframe=pandas_dataframe_with_data,
                          path_or_buffer=buffer)

        text = buffer.getvalue()
        assert isinstance(text, str) is True
        assert len(text) > 0
        assert f'TRUNCATE {table_name}' in text

    def test_replace(self,
                     replace_dataframe,
                     fixture_spec_replace):
        buffer = StringIO()
        sql_writer = SQLFormatter(specification=fixture_spec_replace)
        sql_writer.format(replace_dataframe, buffer)

        table_name = 'My_table'
        text = buffer.getvalue()
        assert isinstance(text, str) is True
        assert len(text) > 0
        assert f'DROP TABLE IF EXISTS {table_name};' in text

    def test_replace_without_schema(self,
                                    replace_dataframe,
                                    fixture_spec_replace_without_schema):
        buffer = StringIO()
        sql_writer = SQLFormatter(
            specification=fixture_spec_replace_without_schema)
        with raises(ValueError):
            sql_writer.format(replace_dataframe, buffer)

    def test_invalid_mode(self, sql_specification_format,
                          pandas_dataframe_with_data):
        buffer = StringIO()
        table_name = 'mytable'
        sql_writer = SQLFormatter(
            specification=sql_specification_format(table_name, mode=''))

        with raises(ValueError):
            sql_writer.format(dataframe=pandas_dataframe_with_data,
                              path_or_buffer=buffer)

    def test_sql_script_is_append2(self,
                                   replace_dataframe,
                                   fixture_spec_append2):
        buffer = StringIO()
        sql_writer = SQLFormatter(
            specification=fixture_spec_append2)
        sql_writer.format(dataframe=replace_dataframe,
                          path_or_buffer=buffer)

        assert "INSERT INTO".lower() in buffer.getvalue().lower()
