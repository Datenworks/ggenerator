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
            if column in schema \
                    and schema.get(column).get('quoted') is True:
                row_value_sql += "'" + str(row[column]) + "'"
            else:
                row_value_sql += str(row[column])
        row_value_sql += ")"
        return row_value_sql

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

    def truncate_statement(self, dataframe, params):
        table_name = params.get("table_name")
        query = f"TRUNCATE {table_name};\n\n"
        query += self.append_statement(dataframe, params)
        return query

    def replace_statement(self, dataframe, params):
        schema = params.get('schema')
        table_name = params.get('table_name')
        fields = "("
        cont = 0
        for new_field in schema:
            sql_type = schema[new_field].get('sqltype')
            fields += new_field + " " + sql_type
            cont += 1
            if cont < len(schema):
                fields += ", "
        fields += ");"
        replace = f"DROP TABLE IF EXISTS {table_name};\n" \
                  f"CREATE TABLE {table_name}" \
                  f"{fields}"
        append = self.append_statement(dataframe, params)
        return f"{replace} \n{append}"
