from src.lib.shell import Shell


class MySQLConnection(object):
    connection = ("--host={host} --port={port} --user={user} "
                  "--password={password}")

    def __init__(self, host, username, password, port, database, **kwargs):
        self.shell = Shell()
        self.base_connection = self.connection.format(
            host=host,
            port=port,
            user=username,
            password=password,
        )
        self.base_connection = self.base_connection.split(" ")
        self.database = database

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def execute_query(self, query, *args):
        command = [
            'mysql',
        ]
        for argoption in self.base_connection:
            command.append(argoption)
        command.append(self.database)
        command.append('-e')
        command.append(query)

        self.shell.execute(command=command)

    def close(self):
        pass
