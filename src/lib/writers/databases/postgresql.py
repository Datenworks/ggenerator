from pandas import DataFrame
from src.lib.writers.databases import DatabaseWriter


class PostgresClientDatabaseWriter(DatabaseWriter):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    def write(self, dataframe: DataFrame):
        pass


class PostgresDirectDatabaseWriter(DatabaseWriter):
    """Class that receive pandas dataframe
    and write it on a SGDB
    """
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.default = {}
        self.specification = specification

    def engine(self, params):
        pass

    def write(self, dataframe: DataFrame) -> None:
        """Write all dataframe on a DataBase Table.

        Keyword arguments:
            - dataframe - pandas.Dataframe: dataframe containing the records
        """
        pass
