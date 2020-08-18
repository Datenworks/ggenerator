from src.lib.shell import Shell
from os import getenv


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

        self.windows_host = f"{host}"
        self.windows_user = f"{user}"
        self.windows_db = f"{database}"
        self.windows_port = f"{port}"

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

    def execute_query_windows(self, query):
        postgres_envvar = getenv("PSQL_CLI_BINPATH")
        #start_command = f"{postgres_envvar} -h localhost -U postgres -d my_db2 -p 5432 -c \"CREATE TABLE teste (id INTEGER)"
        start_command = f"{postgres_envvar} -h {self.windows_host} -U {self.windows_user} -d {self.windows_db} -p {self.windows_port} -c SET CLIENT_ENCODING TO 'UTF8' -c \"{query}"
        start_psql = self.shell \
                         .execute(command=start_command)
        # command = [
        #         # postgres_envvar,
        #         # self.windows_host,
        #         # self.windows_user,
        #         # self.windows_db,
        #         # self.windows_port,
        #         '-c',
        #         query
        #         # 'psql'
        #         # "-hlocalhost",
        #         # "-Upostgres",
        #         # "-dmy_db2",
        #         # "-p5432"
        #         # "postgres"
        #         # "-h localhost -U postgres -d my_db2 -p 5432"
        #     ]
        # output = self.shell \
        #              .execute(command=command)
        return start_psql
