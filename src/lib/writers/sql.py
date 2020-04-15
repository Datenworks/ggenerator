from pandas import DataFrame
from src.lib.writers.sgdb import sgdb_engines_map


class SQLWriter(object):
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

    def write(self, dataframe: DataFrame) -> None:
        """Write all dataframe on a DataBase Table.

        Keyword arguments:
            - dataframe - pandas.Dataframe: dataframe containing the records
        """
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        method = parameters.get('method')

        engine_name = parameters['engine']
        engine_clazz = sgdb_engines_map[engine_name]
        engine = engine_clazz(host=parameters['host'],
                              port=parameters['port'])

        password = self.prompt_password()

        if method == 'direct':
            connection = engine.connect(user=parameters['username'],
                                        password=password,
                                        database=parameters['database'])
            self.formatter.to_sql(dataframe=dataframe,
                                  schema=parameters['schema'],
                                  conn=connection)
        elif method == 'cli':
            engine.cli()  # TODO

    def prompt_password(self):
        return input("SGDB Password")

    @staticmethod
    def rules():
        return {
            'required': {
                'options.engine': {'none': False, 'type': str},
                'options.method': {'none': False, 'type': str},
                'options.host': {'none': False, 'type': str},
                'options.port': {'none': False, 'type': int},
                'options.database': {'none': False, 'type': str},
                'options.username': {'nome': False, 'type': str}
            },
            'optional': {
                'options.schema': {'none': False, 'type': str}
            }}
