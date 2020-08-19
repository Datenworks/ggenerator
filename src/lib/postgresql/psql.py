from os import getenv
from src.lib.shell import Shell

POSTGRES_CLI_BINPATH = getenv("POSTGRES_CLI_BINPATH")


class PostgresSqlPsql(object):
    connection = ("host={host} port={port} user={user} "
                  "password={password} dbname={database}")

    def __init__(self, host, port, database, user, password):
        self.shell = Shell()
        self.base_command = self.connection\
                                .format(host=host,
                                        port=port,
                                        user=user,
                                        password=password,
                                        database=database)

    def execute_query(self, query):
        nl = "\n"
        command = [
            POSTGRES_CLI_BINPATH or 'psql',
            '-c',
            f'{query.replace(nl, "")}',
            self.base_command
        ]
        output = self.shell \
                     .execute(command=command)

        return output
