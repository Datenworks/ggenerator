from src.lib.shell import Shell


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
        command = [
            '/usr/bin/env',
            'psql',
            self.base_command,
            '-c',
            query
        ]
        output = self.shell \
                     .execute(command=command)

        return output
