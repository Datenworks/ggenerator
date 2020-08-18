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
        query2 = "INSERT INTO my_cli_table (id, name, age, weight, job, datetime) VALUES(1, 'Dr. Thomas Nascimento', 110, 55.7, 'Figurinista', '2020-08-29 00:37:55'),(2, 'Srta. Eduarda Nogueira', 86, 67.0, 'Homeopata', '2020-09-10 22:31:16'),(3, 'Luiz Gustavo da Cruz', 90, 92.61, 'Geógrafo', '2020-09-03 15:34:27'),(4, 'Enzo Gabriel Ribeiro', 8, 196.99903, 'Argumentista', '2020-09-04 11:11:09'),(5, 'Isadora Silveira', 96, 178.0, 'Ombudsman', '2020-09-14 22:02:25'),(6, 'Kevin Mendes', 86, 99.428089, 'Guardador de veículos', '2020-09-03 03:38:58'),(7, 'Sr. Davi Castro', 103, 8.6464, 'Necromaquiador', '2020-09-01 00:39:43'),(8, 'Lucas Freitas', 34, 92.7312, 'Sonoplasta', '2020-08-26 07:09:07'),(9, 'Thomas Ramos', 2, 140.0, 'Biólogo', '2020-09-05 01:57:51'),(10, 'Maria Eduarda Dias', 43, 69.19367050078, 'Revisor', '2020-09-06 19:17:47')\""
        test = f"{postgres_envvar} -h localhost -U postgres -d my_db2 -p 5432 --set=PGCLIENTENCODING=UTF8 -c \"{query2}"
        nl = "\n"
        start_command = f"{postgres_envvar} -h {self.windows_host} -U {self.windows_user} -d {self.windows_db} -p {self.windows_port} --set=PGCLIENTENCODING=UTF8 -c \"{query.replace(nl, '')}\""
        print(start_command)
        start_psql = self.shell \
                         .execute(command=test)
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
