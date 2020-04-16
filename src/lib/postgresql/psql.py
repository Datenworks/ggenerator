from src.lib.shell import Shell


class PostgresSqlPsql(object):
    prefix = ('psql -h {host} -p {post} -U {user} '
              '-W {password} -d {database}')

    def __init__(self, host, port, database, user, password):
        self.shell = Shell()
        self.base_command = self.prefix \
                                .format(host=host,
                                        port=port,
                                        user=user,
                                        password=password,
                                        database=database)

    def execute_query(self, query):
        command = f"{self.base_command} -c {query}"
        output = self.shell \
                     .execute(command=command.split())

        return output
