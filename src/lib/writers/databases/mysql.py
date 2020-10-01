from pandas import DataFrame
from sqlalchemy import create_engine
from src.lib.writers.databases import DatabaseWriter
from src.lib.mysql.mysql import MySQLConnection


class MysqlDatabaseWriter(DatabaseWriter):
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


class MysqlClientDatabaseWriter(MysqlDatabaseWriter):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame):
        parameters = self.specification \
                         .get('options')

        sql = self.formatter \
                  .format(dataframe=dataframe,
                          path_or_buffer=None)
        if sql is not None:
            with MySQLConnection(**parameters) as connection:
                for query in sql.split(';'):
                    connection.execute_query(query)

        return "Inserted with success"


class MysqlDirectDatabaseWriter(MysqlDatabaseWriter):
    """Class that receive pandas dataframe
    and write it on a SGDB
    """
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.default = {
            'schema': None
        }
        self.specification = specification

    def engine(self, params):
        return create_engine('mysql+mysqlconnector://'
                             f"{params['username']}:"
                             f"{params['password']}@"
                             f"{params['host']}:"
                             f"{params.get('port', 3306)}/"
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
