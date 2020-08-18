import platform
from os import getenv
from pandas import DataFrame
from sqlalchemy.engine import create_engine

from src.lib.postgresql.psql import PostgresSqlPsql
from src.lib.writers.databases import DatabaseWriter


class PostgreSqlClientDatabaseWriter(DatabaseWriter):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame):
        params = self.specification \
                     .get('options')

        sql = self.formatter \
                  .format(dataframe=dataframe,
                          path_or_buffer=None)
        if sql is not None:
            psql = PostgresSqlPsql(host=params['host'],
                                   port=params.get('port', 5432),
                                   database=params['database'],
                                   user=params['username'],
                                   password=params['password'])
            if platform.system() == "Windows":
                postgres_envvar = getenv("PSQL_CLI_BINPATH")
                # postgres_envvar = getenv("TESTE")
                print(postgres_envvar)
                if postgres_envvar == "" or postgres_envvar == " " \
                        or postgres_envvar is None:
                    raise ValueError(
                        "Please set your PSQL_CLI_BINPATH env var.")
                for query in sql.split(';'):
                    if len(query) < 6:
                        continue
                    psql.execute_query_windows(query)
            elif platform.system() == "Linux":
                for query in sql.split(';'):
                    if len(query) < 6:
                        continue
                    psql.execute_query(query)

        return "Inserted with success"


class PostgresDirectDatabaseWriter(DatabaseWriter):
    """Class that receive pandas dataframe
    and write it on a SGDB
    """
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.default = {
            'schema': 'public'
        }
        self.specification = specification

    def engine(self, params):
        return create_engine('postgres://'
                             f"{params['username']}:"
                             f"{params['password']}@"
                             f"{params['host']}:"
                             f"{params.get('port', 5432)}/"
                             f"{params['database']}")

    def write(self, dataframe: DataFrame) -> None:
        """Write all dataframe on a DataBase Table.

        Keyword arguments:
            - dataframe - pandas.Dataframe: dataframe containing the records
        """
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        connection = self.engine(parameters)

        self.formatter.format(dataframe=dataframe,
                              path_or_buffer=connection,
                              method='direct',
                              schema=parameters['schema'])
        return "Inserted with success"
