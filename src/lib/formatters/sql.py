from pandas import DataFrame

from src.lib.sql import Sql


class SQLFormatter(object):
    """Class that receive pandas dataframe
    and write it down in .sql format
    """
    key = 'sql'
    modes = {'append': 'append',
             'truncate': 'replace',
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
                'options.mode': {'none': False,
                                 'type': str,
                                 'values': ["append", "replace", "truncate"]},
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
                                   'custom': [quoted_rule]}
            }
        }

    def __to_db(self,
                dataframe: DataFrame,
                conn,
                params,
                **kwargs) -> str:
        table_name = params.get("table_name")
        index_flag = params.get("index")
        index_label = params.get("index_label", None)
        batch_size = params.get("batch_size")
        mode = self.modes.get(params.get("mode", 'append'))

        try:
            dataframe.to_sql(con=conn,
                             name=table_name,
                             if_exists=mode,
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
            data = sql.append_statement(dataframe, params)
        elif mode == "replace":
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
