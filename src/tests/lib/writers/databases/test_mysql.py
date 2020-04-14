from src.lib.formatters.sql import SQLFormatter
from src.lib.writers.databases.mysql import MysqlDatabaseWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
from src.tests.lib.writers.databases.fixtures import *  # noqa: F403, F401


class TestMysqlDatabaseWriter(object):
    def test_before_write(self, mocker, sql_formatter, mysql_specification):
        expected = "123"
        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        formatter = SQLFormatter(specification=sql_formatter)
        writer = MysqlDatabaseWriter(formatter=formatter,
                                     specification={'options': {}})
        writer.before_write()

        mock.assert_called()
        assert writer.specification['options']['password'] == expected

    def test_writting_csv_with_records(self,
                                       mocker,
                                       pandas_dataframe_with_data,
                                       sql_formatter,
                                       mysql_specification):
        mock_conn = mocker.patch('MySQLdb.connections.Connection')
        mock_conn.cursor.return_value = lambda x: 0

        formatter = SQLFormatter(specification=sql_formatter)
        writer = MysqlDatabaseWriter(formatter=formatter,
                                     specification=mysql_specification)
        writer.write(dataframe=pandas_dataframe_with_data)

        mock_conn.assert_called()

    def test_writting_dataframe_without_records(self,
                                                mocker,
                                                sql_formatter,
                                                pandas_dataframe_without_data,
                                                mysql_specification):
        mock_conn = mocker.patch('MySQLdb.connections.Connection')
        mock_conn.cursor.return_value = lambda x: 0

        formatter = SQLFormatter(specification={})
        writer = MysqlDatabaseWriter(formatter=formatter,
                                     specification=mysql_specification)
        writer.write(dataframe=pandas_dataframe_without_data)

        mock_conn.assert_not_called()
