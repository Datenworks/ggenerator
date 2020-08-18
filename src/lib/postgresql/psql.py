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
        nl = "\n"
        command = [
            'chcp 1252',
            '|',
            '"C:\\Program Files\\PostgreSQL\\12\\bin\\psql"',
            '-c',
            f'{query.replace(nl, "")}',
            f'{self.base_command}'
        ]
        output = self.shell \
                     .execute(command=command)

        return output
