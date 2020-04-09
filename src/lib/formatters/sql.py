from pandas import DataFrame


class SQLFormatter(object):
    """Class that receive pandas dataframe
    and write it down in CSV format
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
                'options.table_name': {'none': False, 'type': str}
            },
            'optional': {
                'options.sep': {'none': False, 'type': str},
                'options.index': {'none': False, 'type': bool},
                'options.index_label': {'none': False, 'type': str}
            }
        }

    def format(self, dataframe: DataFrame, path_or_buffer) -> str:
        """Format dataframe to csv.

        Parameters:
         - dataframe - pandas.DataFrame: dataframe containing the records.
        """
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        if parameters['index']:
            dataframe[parameters.get('index_label')] = dataframe.index

        if dataframe.shape[0] > 0:
            data = self.__format(options=parameters, dataframe=dataframe)
            if isinstance(path_or_buffer, str):
                with open(path_or_buffer, 'w') as f:
                    f.write(data)
            elif path_or_buffer is None:
                return data
            else:
                path_or_buffer.write(data)

    def replace(self, options: dict):
        pass

    def truncate(self, options: dict):
        pass

    def __format(self, options, dataframe):
        if options.get("mode") == "append":
            return self.append(options, dataframe)

    def append(self, options: dict, dataframe: DataFrame) -> str:
        table_name = options.get("table_name")
        schema = options.get("schema", {})
        batch_size = options['batch_size']
        query = ""
        for index in range(0, dataframe.shape[0], batch_size):
            query += \
                self.insert_statement(dataframe[index:index+batch_size],
                                      table_name,
                                      schema)
            query += ";\n\n"
        return query

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

    def insert_statement(self, dataframe: DataFrame, table_name: str,
                         schema: dict):
        columns = dataframe.columns
        values = self.__parse_rows(dataframe, schema)
        return f"INSERT INTO {table_name} " \
               f"({', '.join(columns)}) \n"\
               "VALUES\n" + ",\n".join(values)

    @staticmethod
    def check(*args, **kwargs):
        return True
