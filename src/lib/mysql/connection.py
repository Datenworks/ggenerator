class MysqlConnection(object):

    def __init__(self, host, username, password, port, database, **kwargs):
        try:
            from MySQLdb import Connect
        except ModuleNotFoundError:
            msg = ("To use MySQL client method you need to "
                   "install `mysqlclient` library: "
                   "https://pypi.org/project/mysqlclient/, "
                   "run: pip install ggenerator[mysql] to install it!")
            raise Exception(msg)

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
