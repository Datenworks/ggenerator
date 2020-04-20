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


@fixture
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
                "id": {
                    "quoted": False,
                    "sqltype": "INTEGER"
                },
                "name": {
                    "quoted": True,
                    "sqltype": "VARCHAR(50)"
                },
                "age": {
                    "quoted": False,
                    "sqltype": "INTEGER"
                }
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
        },
        {
            "id": 2,
            "name": "Davi Lucca Duarte",
            "age": 105,
        },
        {
            "id": 3,
            "name": "Luna da Rosa",
            "age": 56,
        },
        {
            "id": 4,
            "name": "Vitor Melo",
            "age": 74,
        },
        {
            "id": 5,
            "name": "Catarina Correia",
            "age": 6,
        }
    ]
    return pandas_dataframe(data=data)
