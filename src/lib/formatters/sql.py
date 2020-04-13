from pandas import DataFrame


class SQLFormatter(object):
    """Class that receive pandas dataframe
    and write it down in SQL format
    """
    key = 'sql'

    def __init__(self, specification):
        self.default = {
            'mode': 'append',
            'batch_size': 50,
            'index': False
        }
        self.specification = specification

    @staticmethod
    def rules():
        return {
            'required': {
                'options.table_name': {'none': False, 'type': str},
                'options.batch_size': {'none': False, 'type': int},
            },
            'optional': {
                'options.mode': {'none': False, 'type': str},
                'options.index': {'none': False, 'type': bool},
                'options.index_label': {'none': False, 'type': str}
            }
        }

    def format(self, dataframe: DataFrame, path_or_buffer) -> str:
        """Format dataframe to sql script.

        Parameters:
         - dataframe - pandas.DataFrame: dataframe containing the records.
         - path_or_buffer: path-like string or a File handler
        """
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        if dataframe.shape[0] > 0:
            data = self.__format(parameters=parameters, dataframe=dataframe)
            if isinstance(path_or_buffer, str):
                with open(path_or_buffer, 'w') as f:
                    f.write(data)
            elif path_or_buffer is None:
                return data
            else:
                path_or_buffer.write(data)

    def replace(self, options: dict, dataframe):
        table_name = options.get("table_name")
        query = f"DROP TABLE IF EXISTS {table_name};\n\n"
        query += self.append(options, dataframe)
        return query

    def truncate(self, options: dict, dataframe):
        table_name = options.get("table_name")
        query = f"TRUNCATE {table_name};\n\n"
        query += self.append(options, dataframe)
        return query

    def __format(self, parameters, dataframe):
        mode = parameters.get("mode")
        if parameters.get("mode") == "append":
            return self.append(parameters=parameters, dataframe=dataframe)
        elif mode == "replace":
            return self.replace(parameters, dataframe)
        elif mode == "truncate":
            return self.truncate(parameters, dataframe)
        else:
            raise ValueError(f"Mode `{mode}` is invalid, expected:"
                             " 'append', 'truncate' or 'replace'")

    def append(self, parameters: dict, dataframe: DataFrame) -> str:
        table_name = parameters.get("table_name")
        schema = parameters.get("schema", {})
        batch_size = parameters['batch_size']
        query = ""
        for index in range(0, dataframe.shape[0], batch_size):
            query += \
                self.insert_statement(dataframe[index:index+batch_size],
                                      table_name,
                                      schema)
            query += ";\n\n"
        return query

    def insert_statement(self, dataframe: DataFrame,
                         table_name: str,
                         schema: dict):
        columns = dataframe.columns
        values = self.__parse_rows(dataframe, schema)
        return f"INSERT INTO {table_name} " \
               f"({', '.join(columns)}) \n"\
               "VALUES\n" + ',\n'.join(values)

    def __parse_rows(self, dataframe: DataFrame, schema: dict = {}) -> list:
        columns = dataframe.columns
        values = []
        for index, row in dataframe.iterrows():
            values.append(self.__parse_row(row, columns, schema))
        return values

    def __parse_row(self, row, columns, schema: dict = {}):
        row_value_sql = "("
        first_column = True
        for column in columns:
            if not first_column:
                row_value_sql += ", "
            first_column = False
            if column in schema \
                    and schema.get(column).get('quoted'):
                row_value_sql += "'" + str(row[column]) + "'"
            else:
                row_value_sql += str(row[column])
        row_value_sql += ")"
        return row_value_sql
