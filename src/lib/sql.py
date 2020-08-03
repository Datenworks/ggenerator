from pandas import DataFrame


class Sql(object):
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
            if self.is_quoted(column, schema, row[column]):
                row_value_sql += "'" + str(row[column]) + "'"
            else:
                row_value_sql += str(row[column])
        row_value_sql += ")"
        return row_value_sql

    def is_quoted(self, column, schema, value):
        return self.is_text(value) or \
            column in schema and \
            schema.get(column, dict()).get('quoted', False) is True

    def is_text(self, value):
        return isinstance(value, str)

    def insert_statement(self, dataframe: DataFrame,
                         table_name: str,
                         schema: dict):
        columns = dataframe.columns
        values = self.__parse_rows(dataframe, schema)
        return f"INSERT INTO {table_name} " \
               f"({', '.join(columns)}) \n"\
               "VALUES\n" + ',\n'.join(values)

    def append_statement(self, dataframe, params):
        table_name = params.get("table_name")
        schema = params.get("schema", {})
        batch_size = params['batch_size']
        query = ""
        for index in range(0, dataframe.shape[0], batch_size):
            query += \
                self.insert_statement(dataframe[index:index+batch_size],
                                      table_name,
                                      schema)
            query += ";\n\n"
        return query

    def create_append_statement(self, dataframe, params):
        mode = params.get('mode')
        if mode == 'truncate' or mode == 'append':
            query = self.append_statement(dataframe, params)
        else:
            query = self.create_table_statement(params)
            query += self.append_statement(dataframe, params)
        return query

    def truncate_statement(self, dataframe, params):
        table_name = params.get("table_name")
        query = f"TRUNCATE {table_name};\n\n"
        query += self.append_statement(dataframe, params)
        return query

    def replace_statement(self, dataframe, params):
        table_name = params.get('table_name')
        replace = f"DROP TABLE IF EXISTS {table_name};\n"
        replace += self.create_table_statement(params)
        append = self.append_statement(dataframe, params)
        return f"{replace} \n{append}"

    def create_table_statement(self, params):
        schema = params.get('schema')
        table_name = params.get('table_name')
        fields = "("
        cont = 0
        if params.get("index"):
            fields += params.get("index_label") + " INTEGER,"
        for new_field in schema:
            sql_type = schema[new_field].get('sqltype')
            fields += new_field + " " + sql_type
            cont += 1
            if cont < len(schema):
                fields += ", "
        fields += ");"
        return f"CREATE TABLE IF NOT EXISTS {table_name} {fields}\n\n"
