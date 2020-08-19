import platform
from os import getenv

from src.lib.shell import Shell

MYSQL_CLI_BINPATH = getenv("MYSQL_CLI_BINPATH")


class MySQLConnection(object):
    connection = ("--host={host} --port={port} --user={user} "
                  "--password={password}")

    def __init__(self, host, username, password, database, port=3306,
                 **kwargs):
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

    def execute_query(self, query, *args, **kwargs):
        command = [
            MYSQL_CLI_BINPATH or 'mysql',
        ]

        if platform.system() == "Windows":
            command.append("--default-character-set=utf8")

        for argoption in self.base_connection:
            command.append(argoption)
        command.append(self.database)
        command.append('-e')
        command.append(query)

        self.shell.execute(command=command)

    def close(self):
        pass
