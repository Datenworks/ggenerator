import pandas as pd

from sqlalchemy import create_engine

from src.lib.formatters.sql import SQLFormatter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
from src.tests.lib.writers.databases.fixtures import *  # noqa: F403, F401
from src.lib.writers.databases.postgresql import PostgresDirectDatabaseWriter


class TestPostgresDirectDatabaseWriter(object):
    def test_before_write(self, mocker, sql_specification_format):
        expected = "123"
        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = PostgresDirectDatabaseWriter(formatter=formatter,
                                              specification={'options': {}})
        writer.before_write()

        mock.assert_called()
        assert writer.specification['options']['password'] == expected

    def test_writting_csv_with_records(self,
                                       mocker,
                                       pandas_dataframe_with_data,
                                       sql_specification_format,
                                       postgres_specification_direct):
        db_engine = create_engine('sqlite:///:memory:')

        mock = mocker.patch('getpass._raw_input')
        mock.return_value = "mytable"

        mock_ = mocker.patch.object(PostgresDirectDatabaseWriter, 'engine')
        mock_.return_value = db_engine

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = PostgresDirectDatabaseWriter(
            formatter=formatter,
            specification=postgres_specification_direct)
        writer.before_write()
        writer.write(dataframe=pandas_dataframe_with_data)

        dataframe_from_sql = pd.read_sql_table(
            table_name='mytable', con=db_engine)
        assert dataframe_from_sql.equals(pandas_dataframe_with_data)
        mock_.assert_called()

    def test_writting_dataframe_without_records(self,
                                                mocker,
                                                sql_specification_format,
                                                pandas_dataframe_without_data,
                                                postgres_specification_direct):
        mock_conn = mocker.patch('psycopg2.connect')
        mock_conn.cursor.return_value = lambda x: 0

        formatter = SQLFormatter(specification={})
        writer = PostgresDirectDatabaseWriter(
            formatter=formatter,
            specification=postgres_specification_direct)
        writer.write(dataframe=pandas_dataframe_without_data)

        mock_conn.assert_not_called()
