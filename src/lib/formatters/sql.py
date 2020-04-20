from pandas import DataFrame
from sqlalchemy.engine import Engine
from src.lib.sql import Sql


class SQLFormatter(object):
    """Class that receive pandas dataframe
    and write it down in .sql format
    """
    key = 'sql'
    modes = {'append': 'append',
             'truncate': 'append',
             'replace': 'replace'}

    def __init__(self, specification):
        self.default = {
            'mode': 'append',
            'batch_size': 50,
            'index': False
        }
        self.specification = specification

    @staticmethod
    def rules():
        def replace_rule(options):
            schema = options.get("schema")
            for key in schema.keys():
                field = schema.get(key)
                mode = options.get("mode")
                if mode == "replace":
                    if not isinstance(field.get("sqltype", None), str):
                        raise ValueError(
                            "The Mode replace needs "
                            "'sqltype' in Schema fields")

        def quoted_rule(schema):
            for key in schema.keys():
                field = schema.get(key)
                if not isinstance(field.get("quoted", None), bool):
                    raise ValueError(" Schema fields required 'quoted'")

        return {
            'required': {
                'options.table_name': {'none': False, 'type': str},
                'options': {'none': False,
                            'type': dict,
                            'custom': [replace_rule]}
            },
            'optional': {
                'options.batch_size': {'none': False, 'type': int},
                'options.index': {'none': False, 'type': bool},
                'options.index_label': {'none': False, 'type': str},
                'options.schema': {'none': False,
                                   'type': dict,
                                   'custom': [quoted_rule]},
                'options.mode': {'none': False,
                                 'type': str,
                                 'values': ["append", "replace", "truncate"]}
            }
        }

    def __to_db(self,
                dataframe: DataFrame,
                conn: Engine,
                params,
                **kwargs) -> str:
        table_name = params.get("table_name")
        index_flag = params.get("index")
        index_label = params.get("index_label", None)
        batch_size = params.get("batch_size")
        mode = params.get("mode", 'append')

        try:
            if mode == 'truncate' and conn.has_table(table_name=table_name):
                conn.execution_options(autoCommit=True)\
                    .execute(f"""TRUNCATE TABLE {table_name}""")
            dataframe.to_sql(con=conn,
                             name=table_name,
                             if_exists=self.modes.get(mode),
                             index=index_flag,
                             index_label=index_label,
                             chunksize=batch_size,
                             **kwargs)
        except Exception as err:
            msg = ("Error: Check your credentials (username,"
                   " password, host, port, database)\n")
            raise ValueError(msg, err)

    def __to_sql(self,
                 dataframe: DataFrame,
                 path_or_buffer,
                 params,
                 **kwargs) -> str:
        sql = Sql()
        mode = params.get("mode")

        if params.get('index'):
            dataframe.index.name = params.get('index_label')
            dataframe = dataframe.reset_index(level=0)

        if mode == "append":
            data = sql.create_append_statement(dataframe, params)
        elif mode == "replace":
            schema = params.get('schema')
            dataframe_columns = dataframe.columns
            for column in dataframe_columns:
                if column not in schema:
                    raise ValueError("Schema must have the same field names"
                                     " to create the new table")
            for schema_field in schema:
                if schema_field not in dataframe_columns:
                    raise ValueError(
                        f"{schema_field} not found in fields generator. "
                        "Please remove it from Schema"
                        f" or insert the {schema_field} generator")
            data = sql.replace_statement(dataframe, params)
        elif mode == "truncate":
            data = sql.truncate_statement(dataframe, params)
        else:
            raise ValueError(f"Mode `{mode}` is invalid, expected:"
                             " 'append', 'truncate' or 'replace'")

        if isinstance(path_or_buffer, str):
            with open(path_or_buffer, 'w') as f:
                f.write(data)
        elif path_or_buffer is None:
            return data
        else:
            path_or_buffer.write(data)

    def format(self,
               dataframe: DataFrame,
               path_or_buffer,
               method=None,
               **kwargs) -> str:
        """Format dataframe to sql script.

        Parameters:
         - dataframe - pandas.DataFrame: dataframe containing the records.
         - path_or_buffer: path-like string or a File handler
        """
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        if dataframe.shape[0] > 0:
            if method == 'direct':
                return self.__to_db(dataframe=dataframe,
                                    conn=path_or_buffer,
                                    params=parameters,
                                    **kwargs)
            return self.__to_sql(dataframe=dataframe,
                                 path_or_buffer=path_or_buffer,
                                 params=parameters,
                                 **kwargs)
