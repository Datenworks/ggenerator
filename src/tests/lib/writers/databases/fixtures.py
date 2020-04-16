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
def postgres_specification():
    return {
        "type": "sql",
        "options": {
            "engine": "postgres",
            "method": "direct",
            "host": "",
            "port": 3306,
            "database": "",
            "schema": "",
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
