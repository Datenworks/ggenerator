from getpass import getpass
from pandas import DataFrame

from src.lib.postgresql.psql import PostgresSqlPsql


class PostgreSqlClientDatabaseWriter(object):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def before_write(self):
        host = self.specification \
                   .get('options') \
                   .get('host')
        user = self.specification \
                   .get('options') \
                   .get('username')
        print(f"Database host: {host}")
        print(f"Username: {user}")
        self.specification['options']['password'] = \
            getpass(f"Type {user} password: ")

    @staticmethod
    def rules():
        return {
            'required': {
                'options.engine': {'none': False, 'type': str},
                'options.host': {'none': False, 'type': str},
                'options.database': {'none': False, 'type': str},
                'options.username': {'none': False, 'type': str}
            },
            'optional': {
                'options.method': {'none': False, 'type': str},
                'options.port': {'none': False, 'type': int},
                'options.schema': {'none': False, 'type': str}
            }
        }

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
            for query in sql.split(';'):
                if len(query) < 6:
                    continue
                psql.execute_query(query)

        return "Inserted with success"
