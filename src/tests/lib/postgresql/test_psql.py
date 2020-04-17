from pytest import raises
from subprocess import Popen

from src.lib.postgresql.psql import PostgresSqlPsql
from src.lib.shell import ShellError


class TestPostgreSqlPsql(object):
    def test_execute_success(self, mocker):
        query = ''
        expected = b'', None

        mock = mocker.patch.object(Popen, 'communicate')
        mock.return_value = expected

        psql = PostgresSqlPsql(host='',
                               port='',
                               database='',
                               user='',
                               password='')
        query_result = psql.execute_query(query)

        mock.assert_called()
        assert query_result == expected[0].decode()

    def test_execute_failure(self, mocker):
        query = ''
        expected = b'', True

        mock = mocker.patch.object(Popen, 'communicate')
        mock.return_value = expected

        psql = PostgresSqlPsql(host='',
                               port='',
                               database='',
                               user='',
                               password='')
        with raises(ShellError):
            psql.execute_query(query)

        mock.assert_called()
