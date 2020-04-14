from getpass import getpass
from pandas import DataFrame

from src.lib.mysql.connection import MysqlConnection


class MysqlDatabaseWriter(object):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def rules():
        return {
            'required': {
                'options.host': {'none': False, 'type': str},
                'options.username': {'none': False, 'type': str},
                'options.database': {'none': False, 'type': str}
            },
            'optional': {
                'options.port': {'none': False, 'type': str},
                'options.schema': {'none': False, 'type': str}
            }
        }

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

    def write(self, dataframe: DataFrame):
        row_count = 0
        parameters = self.specification \
                         .get('options')

        sql = self.formatter \
                  .format(dataframe=dataframe,
                          path_or_buffer=None)
        if sql is not None:
            with MysqlConnection(**parameters) as connection:
                for query in sql.split(';'):
                    if len(query) < 6:
                        continue
                    row_count += connection.execute_query(query)

        return f"{row_count} rows inserted"
