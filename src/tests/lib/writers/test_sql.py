import pandas as pd

from sqlalchemy import create_engine

from src.lib.formatters.sql import SQLFormatter
from src.lib.writers.databases.mysql import MysqlDirectDatabaseWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
import os
import uuid


class TestSQLWriter(object):
    """Unit-test for SQLWriter class"""

    def test_writting_sql_table_without_index(self,
                                              mocker,
                                              pandas_dataframe_with_data,
                                              specification,
                                              sql_specification_format,
                                              sql_specification_writer):
        expected = "123456789"
        table_name = "mytable"
        index_flag = False
        formatter_spec = sql_specification_format(table_name=table_name,
                                                  index=index_flag)

        formatter = SQLFormatter(specification=formatter_spec)
        writer = MysqlDirectDatabaseWriter(
            formatter=formatter,
            specification=sql_specification_writer
        )

        db_engine = create_engine('sqlite:///:memory:')

        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        mock_ = mocker.patch.object(MysqlDirectDatabaseWriter, 'engine')
        mock_.return_value = db_engine

        writer.before_write()
        writer.write(dataframe=pandas_dataframe_with_data)

        dataframe_from_sql = pd.read_sql_table(
            table_name='mytable', con=db_engine)
        assert dataframe_from_sql.equals(pandas_dataframe_with_data)
        mock_.assert_called()

    def test_writting_sql_table_with_index(self,
                                           mocker,
                                           pandas_dataframe_with_data,
                                           specification,
                                           sql_specification_format,
                                           sql_specification_writer):
        expected = "123456789"
        table_name = "mytable"
        index_flag = True
        index_label = "myindexlabel"
        formatter_spec = sql_specification_format(table_name=table_name,
                                                  index=index_flag,
                                                  index_label=index_label)

        formatter = SQLFormatter(specification=formatter_spec)
        writer = MysqlDirectDatabaseWriter(
            formatter=formatter,
            specification=sql_specification_writer
        )

        db_engine = create_engine('sqlite:///:memory:')

        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        mock_ = mocker.patch.object(MysqlDirectDatabaseWriter, 'engine')
        mock_.return_value = db_engine

        writer.before_write()
        writer.write(dataframe=pandas_dataframe_with_data)

        pandas_dataframe_with_data.index.name = index_label
        pandas_dataframe_with_data = \
            pandas_dataframe_with_data.reset_index(level=0)

        dataframe_from_sql = pd.read_sql_table(
            table_name='mytable', con=db_engine)
        assert dataframe_from_sql.equals(pandas_dataframe_with_data)
        mock_.assert_called()

    def test_writing_sql_script(self, sql_specification_format,
                                pandas_dataframe_with_data):
        table_name = "mytable"
        index_flag = True
        index_label = "myindexlabel"
        uri = uuid.uuid4().hex
        formatter_spec = sql_specification_format(table_name=table_name,
                                                  index=index_flag,
                                                  index_label=index_label)
        formatter = SQLFormatter(specification=formatter_spec)
        formatter.format(dataframe=pandas_dataframe_with_data,
                         path_or_buffer=uri)

        assert os.path.exists(uri)
        with open(uri, 'r') as f:
            assert len(f.read()) > 0
        os.remove(uri)
