from pandas import DataFrame

from src.lib.mysql.connection import MysqlConnection


class MysqlDatabaseWriter(object):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def rules(self):
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

    def write(self, dataframe: DataFrame):
        parameters = self.specification \
                         .get('options')

        with MysqlConnection(**parameters) as connection:
            query = self.formatter \
                        .format(dataframe=dataframe)
            return connection.execute_query(query)
