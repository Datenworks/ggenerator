from src.lib.formatters.sql import SQLFormatter
from src.lib.writers.sql import SQLWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
from src.lib.writers.sgdb.engines.mysql import MySQLEngine
from sqlalchemy import create_engine
import pandas as pd


class TestSQLWriter(object):
    """Unit-test for SQLWriter class"""

    def test_writting_sql_table_without_index(self,
                                              mocker,
                                              pandas_dataframe_with_data,
                                              specification,
                                              sql_specification_format,
                                              sql_specification_writer):
        table_name = "mytable"
        index_flag = False
        formatter_spec = sql_specification_format(table_name=table_name,
                                                  index=index_flag)

        formatter = SQLFormatter(specification=formatter_spec)
        writer = SQLWriter(formatter=formatter,
                           specification=sql_specification_writer)

        db_engine = create_engine('sqlite:///:memory:')

        mock = mocker.patch.object(SQLWriter, 'prompt_password')
        mock.return_value = "123456789"

        mock_ = mocker.patch.object(MySQLEngine, 'connect')
        mock_.return_value = db_engine

        writer.write(dataframe=pandas_dataframe_with_data)

        dataframe_from_sql = pd.read_sql_table(
            table_name='mytable', con=db_engine)
        assert dataframe_from_sql.equals(pandas_dataframe_with_data)

    def test_writting_sql_table_with_index(self,
                                           mocker,
                                           pandas_dataframe_with_data,
                                           specification,
                                           sql_specification_format,
                                           sql_specification_writer):
        table_name = "mytable"
        index_flag = True
        index_label = "myindexlabel"
        formatter_spec = sql_specification_format(table_name=table_name,
                                                  index=index_flag,
                                                  index_label=index_label)

        formatter = SQLFormatter(specification=formatter_spec)
        writer = SQLWriter(formatter=formatter,
                           specification=sql_specification_writer)

        db_engine = create_engine('sqlite:///:memory:')

        mock = mocker.patch.object(SQLWriter, 'prompt_password')
        mock.return_value = "123456789"

        mock_ = mocker.patch.object(MySQLEngine, 'connect')
        mock_.return_value = db_engine

        writer.write(dataframe=pandas_dataframe_with_data)

        pandas_dataframe_with_data.index.name = index_label
        pandas_dataframe_with_data = \
            pandas_dataframe_with_data.reset_index(level=0)

        dataframe_from_sql = pd.read_sql_table(
            table_name='mytable', con=db_engine)
        assert dataframe_from_sql.equals(pandas_dataframe_with_data)
