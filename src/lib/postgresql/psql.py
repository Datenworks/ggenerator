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

        self.windows_host = f"-h{host}"
        self.windows_user = f"-U{user}"
        self.windows_db = f"-d{database}"
        self.windows_port = f"-p{port}"

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

    def execute_query_windows(self, query, postgres_envvar):
        command = [
                postgres_envvar,
                self.windows_host,
                self.windows_user,
                self.windows_db,
                self.windows_port
                # 'psql'
                # "-hlocalhost",
                # "-Upostgres",
                # "-dmy_db2",
                # "-p5432"
                # "postgres"
                # "-h localhost -U postgres -d my_db2 -p 5432"
            ]
        output = self.shell \
                     .execute(command=command)
        return output
