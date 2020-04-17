from pandas import DataFrame
from sqlalchemy.engine import create_engine

from src.lib.writers.databases import DatabaseWriter


class PostgresDirectDatabaseWriter(DatabaseWriter):
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
        return create_engine('postgres://'
                             f"{params['username']}:"
                             f"{params['password']}@"
                             f"{params['host']}:"
                             f"{params['port']}/"
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
