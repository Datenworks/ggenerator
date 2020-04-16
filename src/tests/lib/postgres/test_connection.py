from src.lib.postgres.connection import PostgresConnection


class TestPostgresConnection(object):

    def test_execute(self, mocker):
        mock_conn = mocker.patch('psycopg2.connections.Connection')
        mock_conn.cursor.return_value = lambda x: 0

        with PostgresConnection(host='',
                                username='',
                                password='',
                                port=3306,
                                database_name='') as conn:
            conn.execute_query('')
        mock_conn.assert_called()
