from src.lib.formatters.sql import SQLFormatter
from src.lib.postgresql.psql import PostgresSqlPsql
from src.lib.writers.databases.postgresql import PostgreSqlClientDatabaseWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
from src.tests.lib.writers.databases.fixtures import *  # noqa: F403, F401


class TestPostgreSqlClientDatabaseWriter(object):
    def test_before_write(self, mocker, sql_specification_format):
        expected = "123"
        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = PostgreSqlClientDatabaseWriter(
            formatter=formatter,
            specification={'options': {}}
        )
        writer.before_write()

        mock.assert_called()
        assert writer.specification['options']['password'] == expected

    def test_writting_csv_with_records(self,
                                       mocker,
                                       pandas_dataframe_with_data,
                                       sql_specification_format,
                                       postgres_specification_cli):
        mock_conn = mocker.patch.object(PostgresSqlPsql, 'execute_query')
        mock_conn.return_value = lambda x: None

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = PostgreSqlClientDatabaseWriter(
            formatter=formatter,
            specification=postgres_specification_cli
        )
        writer.write(dataframe=pandas_dataframe_with_data)

        mock_conn.assert_called()

    def test_writting_dataframe_without_records(self,
                                                mocker,
                                                pandas_dataframe_without_data,
                                                postgres_specification_cli):
        mock_conn = mocker.patch.object(PostgresSqlPsql, 'execute_query')
        mock_conn.return_value = lambda x: None

        formatter = SQLFormatter(specification={})
        writer = PostgreSqlClientDatabaseWriter(
            formatter=formatter,
            specification=postgres_specification_cli
        )
        writer.write(dataframe=pandas_dataframe_without_data)

        mock_conn.assert_not_called()
