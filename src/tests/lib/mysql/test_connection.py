from src.lib.mysql.mysql import MySQLConnection


class TestMysqlConnection(object):

    def test_execute(self, mocker):
        mock_conn = mocker.patch('src.lib.shell.Shell.execute')
        mock_conn.cursor.return_value = lambda x: 0

        with MySQLConnection(host='',
                             username='',
                             password='',
                             port=3306,
                             database='') as conn:
            conn.execute_query('')

        mock_conn.assert_called()
