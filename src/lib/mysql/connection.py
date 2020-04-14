from MySQLdb import Connect


class MysqlConnection(object):

    def __init__(self, host, username, password, port, database, **kwargs):
        self.connection = Connect(host=host,
                                  user=username,
                                  passwd=password,
                                  port=port,
                                  db=database)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def execute_query(self, query, *args):
        with self.connection \
                 .cursor() as cursor:
            query_result = cursor.execute(query, *args)

        self.connection.commit()
        return query_result

    def close(self):
        self.connection.close()
