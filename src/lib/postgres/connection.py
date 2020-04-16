import psycopg2


class PostgresConnection(object):

    def __init__(self, host, username, password, port, database_name,
                 **kwargs):
        #  sudo apt-get install libpq-dev
        self.connection = psycopg2.connect(host=host,
                                           user=username,
                                           password=password,
                                           port=port,
                                           database=database_name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def execute_query(self, query, *args):
        with self.connection.cursor() as cursor:
            query_result = cursor.execute(query, *args)

        self.connection.commit()
        return query_result

    def close(self):
        self.connection.close()
