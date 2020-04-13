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

    def to_sql(self, dataframe: DataFrame, schema: str, conn) -> str:
        parameters = self.default
        options = self.specification.get('options', {})
        parameters.update(options)

        table_name = parameters.get("table_name")
        index_flag = parameters.get("index")
        index_label = parameters.get("index_label", None)
        batch_size = parameters.get("batch_size")
        mode = parameters.get("mode")

        try:
            dataframe.to_sql(con=conn,
                             name=table_name,
                             schema=schema,
                             if_exists=mode,
                             index=index_flag,
                             index_label=index_label,
                             chunksize=batch_size)
        except Exception as err:
            Exception(err)

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

    def replace(self, options: dict):
        pass

    def truncate(self, options: dict):
        pass

    def __format(self, parameters, dataframe):
        if parameters.get('index'):
            dataframe.index.name = parameters.get('index_label')
            dataframe = dataframe.reset_index(level=0)

        if parameters.get("mode") == "append":
            return self.append(parameters=parameters, dataframe=dataframe)

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

    def insert_statement(self, dataframe: DataFrame, table_name: str,
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

    @staticmethod
    def check(*args, **kwargs):
        return True
