import pandas as pd

from sqlalchemy import create_engine

from src.lib.formatters.sql import SQLFormatter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
from src.tests.lib.writers.databases.fixtures import *  # noqa: F403, F401
from src.lib.writers.databases.postgresql import PostgresDirectDatabaseWriter


class TestPostgresDirectDatabaseWriter(object):
    def test_before_write(self, mocker, sql_formatter, postgres_specification):
        expected = "123"
        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        formatter = SQLFormatter(specification=sql_formatter)
        writer = PostgresDirectDatabaseWriter(formatter=formatter,
                                              specification={'options': {}})
        writer.before_write()

        mock.assert_called()
        assert writer.specification['options']['password'] == expected

    def test_writting_dataframe_with_records(self,
                                             mocker,
                                             pandas_dataframe_with_data,
                                             sql_specification_format,
                                             postgres_specification):
        db_engine = create_engine('sqlite:///:memory:')

        mock = mocker.patch('getpass._raw_input')
        mock.return_value = "mytable"

        mock_ = mocker.patch.object(PostgresDirectDatabaseWriter, 'engine')
        mock_.return_value = db_engine

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = PostgresDirectDatabaseWriter(
            formatter=formatter,
            specification=postgres_specification)
        writer.before_write()
        writer.write(dataframe=pandas_dataframe_with_data)

        dataframe_from_sql = pd.read_sql_table(
            table_name='mytable', con=db_engine)
        assert dataframe_from_sql.equals(pandas_dataframe_with_data)
        mock_.assert_called()

    def test_writting_dataframe_without_records(self,
                                                mocker,
                                                sql_formatter,
                                                pandas_dataframe_without_data,
                                                postgres_specification):
        mock_ = mocker.patch.object(pd.DataFrame, 'to_sql')
        mock_.return_value = 'direct_connection'

        formatter = SQLFormatter(specification={})
        writer = PostgresDirectDatabaseWriter(
            formatter=formatter,
            specification=postgres_specification)
        writer.write(dataframe=pandas_dataframe_without_data)

        mock_.assert_not_called()
