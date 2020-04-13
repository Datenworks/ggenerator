from src.lib.formatters.sql import SQLFormatter
from src.lib.writers.sql import SQLWriter
from src.tests.lib.writers.fixtures import *  # noqa: F403, F401


class TestSQLWriter(object):
    """Unit-test for SQLWriter class"""

    def test_writting_sql_table_with_records(self,
                                             mocker,
                                             pandas_dataframe_with_data,
                                             specification):
        formatter = SQLFormatter(specification={
            'options': {
                'table_name': 'mytable',
                'batch_size': 2,
                'schema': {
                    'Column1': {
                        'quoted': True
                    }
                },
                'mode': 'replace',
                'index': True,
                'index_label': 'meuindicedoido'
            }
        })
        writer = SQLWriter(formatter=formatter, specification={
            'options': {
                'engine': 'mysql',
                'method': 'direct',
                'host': '172.17.0.2',
                'port': 3306,
                'database': 'mydb',
                'username': 'root'
            }
        })

        mock = mocker.patch.object(SQLWriter, 'prompt_password')
        mock.return_value = "123456789"
        writer.write(dataframe=pandas_dataframe_with_data)
