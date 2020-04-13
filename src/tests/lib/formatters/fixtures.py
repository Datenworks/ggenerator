from pytest import fixture


def pandas_dataframe(data):
    from pandas import DataFrame

    dataframe = DataFrame(data=data)

    return dataframe


@fixture
def pandas_dataframe_with_data():
    data = [{"Column": "Value_1", "Column2": "Value_12"},
            {"Column": "Value_2", "Column2": "Value_12"},
            {"Column": "Value_3", "Column2": "Value_12"},
            {"Column": "Value_4", "Column2": "Value_12"},
            {"Column": "Value_5", "Column2": "Value_12"},
            {"Column": "Value_6", "Column2": "Value_12"}]
    return pandas_dataframe(data=data)


@fixture
def pandas_dataframe_without_data():
    return pandas_dataframe(data=[])


@fixture
def fixture_spec_default():
    specification = {
        "datasets": {
            "sample": {
                "size": 10,
                "locale": "pt_BR",
                "fields": [
                    {
                        "type": "integer:sequence",
                        "name": "id",
                        "generator": {
                            "start_at": 1
                        }
                    },
                    {
                        "type": "name",
                        "name": "nome",
                        "generator": {}
                    },
                    {
                        "type": "pyint",
                        "name": "idade",
                        "generator": {
                            "max_value": 120
                        }
                    },
                    {
                        "type": "pyfloat",
                        "name": "peso",
                        "generator": {
                            "positive": 'false',
                            "min_value": 0,
                            "max_value": 250
                        }
                    },
                    {
                        "type": "job",
                        "name": "trabalho",
                        "generator": {}
                    },
                    {
                        "type": "future_datetime",
                        "name": "data",
                        "generator": {}
                    }
                ],
                "format": {
                    "type": "sql",
                    "options": {
                        "index": 'false',
                        "table_name": "My_table",
                        "mode": "append"
                    }
                },
                "serializers": {
                    "to": [
                        {
                            "type": "file",
                            "uri": "/home/tadeu/Desktop/dataset.sql"
                        }
                    ]
                }
            }
        }
    }

    return specification


@fixture
def fixture_spec_replace():
    true = True
    false = False
    specification = {"options": {
        "table_name": "My_table",
        "mode": "replace",
        "schema": {
            "id": {"sqltype": "INTEGER NOT NULL", "quoted":
                   false},
            "name": {"sqltype": "VARCHAR(50)", "quoted":
                     false},
            "age": {"sqltype": "INTEGER NOT NULL", "quoted":
                    false},
            "weight": {"sqltype": "INTEGER NOT NULL", "quoted":
                       true},
            "job": {"sqltype": "VARCHAR(50)", "quoted":
                    false},
            "datetime": {"sqltype": "DATETIME", "quoted":
                         false}
        }

    }
    }

    return specification


@fixture
def replace_dataframe():
    data = [
        {
            "id": 1,
            "nome": "Sophie Silveira",
            "idade": 65,
            "peso": 194.16350529,
            "trabalho": "Fisioterapeuta",
            "data": 1587241737000
        },
        {
            "id": 2,
            "nome": "Davi Lucca Duarte",
            "idade": 105,
            "peso": 19.41,
            "trabalho": "Cabo",
            "data": 1588771828000
        },
        {
            "id": 3,
            "nome": "Luna da Rosa",
            "idade": 56,
            "peso": 104.987,
            "trabalho": "Faxineiro",
            "data": 1588995002000
        },
        {
            "id": 4,
            "nome": "Vitor Melo",
            "idade": 74,
            "peso": 170.79,
            "trabalho": "Sociólogo",
            "data": 1587715890000
        },
        {
            "id": 5,
            "nome": "Catarina Correia",
            "idade": 6,
            "peso": 178.9275,
            "trabalho": "Médico geneticista",
            "data": 1588948730000
        }
    ]
    return pandas_dataframe(data=data)
