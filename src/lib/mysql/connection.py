from MySQLdb import Connect


class MysqlConnection(object):

    def __init__(self, host, user, password, port, database):
        self.connection = Connect(host=host,
                                  user=user,
                                  passwd=password,
                                  port=port,
                                  db=database)

    def __exit__(self, type, value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def execute_query(self, query, *args):
        with self.connection \
                 .cursor() as cursor:
            cursor.execute(query, *args)
            query_result = cursor.info()

        self.connection.commit()
        return query_result

    def close(self):
        self.connection.close()
