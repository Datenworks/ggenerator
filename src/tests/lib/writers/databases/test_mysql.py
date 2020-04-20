from src.lib.formatters.sql import SQLFormatter
from src.lib.writers.databases.mysql import MysqlClientDatabaseWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401
from src.tests.lib.writers.databases.fixtures import *  # noqa: F403, F401


class TestMysqlClientDatabaseWriter(object):
    def test_before_write(self, mocker,
                          sql_specification_format,
                          mysql_specification):
        expected = "123"
        mock = mocker.patch('getpass._raw_input')
        mock.return_value = expected

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = MysqlClientDatabaseWriter(formatter=formatter,
                                           specification={'options': {}})
        writer.before_write()

        mock.assert_called()
        assert writer.specification['options']['password'] == expected

    def test_writting_csv_with_records(self,
                                       mocker,
                                       pandas_dataframe_with_data,
                                       sql_specification_format,
                                       mysql_specification):
        mock_conn = mocker.patch('src.lib.shell.Shell.execute')
        mock_conn.cursor.return_value = lambda x: 0

        formatter = SQLFormatter(
            specification=sql_specification_format('mytable'))
        writer = MysqlClientDatabaseWriter(formatter=formatter,
                                           specification=mysql_specification)
        writer.write(dataframe=pandas_dataframe_with_data)

        mock_conn.assert_called()

    def test_writting_dataframe_without_records(self,
                                                mocker,
                                                pandas_dataframe_without_data,
                                                mysql_specification):
        mock_conn = mocker.patch('src.lib.shell.Shell.execute')
        mock_conn.cursor.return_value = lambda x: 0

        formatter = SQLFormatter(specification={})
        writer = MysqlClientDatabaseWriter(formatter=formatter,
                                           specification=mysql_specification)
        writer.write(dataframe=pandas_dataframe_without_data)

        mock_conn.assert_not_called()
