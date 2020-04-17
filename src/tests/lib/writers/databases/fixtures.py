from pytest import fixture
from src.tests.lib.formatters.fixtures import pandas_dataframe


@fixture
def mysql_specification():
    return {
        "type": "sql",
        "options": {
            "engine": "mysql",
            "method": "cli",
            "host": "",
            "port": 3306,
            "database": "",
            "schema": "",
            "username": "",
            "password": ""
        }
    }


@fixture
def mysql_specification_script():
    return {
        "type": "file",
        "uri": "path/to/file.sql"
    }


def postgres_specification():
    return {
        "type": "sql",
        "options": {
            "engine": "postgres",
            "method": "direct",
            "host": "",
            "port": 3306,
            "database": "",
            "username": "",
            "password": ""
        }
    }


@fixture
def sql_formatter():
    return {
        'options': {
            'table_name': 'mytable',
            "mode": "truncate",
            'batch_size': 2,
            'schema': {
                'Column': {'quoted': True}
            }
        }
    }


@fixture
def dataframe():
    data = [
        {
            "id": 1,
            "name": "Sophie Silveira",
            "age": 65,
            "weight": 194.16350529,
            "job": "Fisioterapeuta",
            "datetime": 1587241737000
        },
        {
            "id": 2,
            "name": "Davi Lucca Duarte",
            "age": 105,
            "weight": 19.41,
            "job": "Cabo",
            "datetime": 1588771828000
        },
        {
            "id": 3,
            "name": "Luna da Rosa",
            "age": 56,
            "weight": 104.987,
            "job": "Faxineiro",
            "datetime": 1588995002000
        },
        {
            "id": 4,
            "name": "Vitor Melo",
            "age": 74,
            "weight": 170.79,
            "job": "Sociólogo",
            "datetime": 1587715890000
        },
        {
            "id": 5,
            "name": "Catarina Correia",
            "age": 6,
            "weight": 178.9275,
            "job": "Médico geneticista",
            "datetime": 1588948730000
        }
    ]
    return pandas_dataframe(data=data)
