from src.lib.mysql.connection import MysqlConnection


class TestMysqlConnection(object):

    def test_execute(self, mocker):
        mock_conn = mocker.patch('MySQLdb.connections.Connection')
        mock_conn.cursor.return_value = lambda x: 0

        with MysqlConnection(host='',
                             username='',
                             password='',
                             port=3306,
                             database='') as conn:
            conn.execute_query('')

        mock_conn.assert_called()
