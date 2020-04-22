from pytest import raises

from src.lib.postgresql.psql import PostgresSqlPsql
from src.lib.shell import ShellError
from src.lib.shell import Shell


class TestPostgreSqlPsql(object):
    def test_execute_success(self, mocker):
        query = ''
        expected = 0, b'', None

        mock = mocker.patch.object(Shell, 'execute_command')
        mock.return_value = expected

        psql = PostgresSqlPsql(host='',
                               port='',
                               database='',
                               user='',
                               password='')
        query_result = psql.execute_query(query)

        mock.assert_called()
        assert query_result == expected[1].decode()

    def test_execute_failure(self, mocker):
        query = ''
        expected = 1, b'', b'Error'

        mock = mocker.patch.object(Shell, 'execute_command')
        mock.return_value = expected

        psql = PostgresSqlPsql(host='',
                               port='',
                               database='',
                               user='',
                               password='')
        with raises(ShellError):
            psql.execute_query(query)

        mock.assert_called()
