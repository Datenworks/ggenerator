from src.tests.lib.formatters.fixtures import pandas_dataframe
from pytest import fixture


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
def postgres_specification_cli():
    return {
        "type": "sql",
        "options": {
            "engine": "postgres",
            "method": "cli",
            "host": "",
            "port": 5432,
            "database": "",
            "username": "",
            "password": ""
        }
    }


@fixture
def postgres_specification_direct():
    return {
        "type": "sql",
        "options": {
            "engine": "postgres",
            "method": "direct",
            "host": "",
            "port": 5432,
            "schema": None,
            "database": "",
            "username": "",
            "password": ""
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
