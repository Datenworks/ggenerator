from pytest import fixture


def pandas_dataframe(data):
    from pandas import DataFrame

    dataframe = DataFrame(data=data)

    return dataframe


@fixture
def pandas_dataframe_with_data():
    data = [{"Column1": "Value_1", "Column2": "Value_12"},
            {"Column1": "Value_2", "Column2": "Value_12"},
            {"Column1": "Value_3", "Column2": "Value_12"},
            {"Column1": "Value_4", "Column2": "Value_12"},
            {"Column1": "Value_5", "Column2": "Value_12"},
            {"Column1": "Value_6", "Column2": "Value_12"}]
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
                     true},
            "age": {"sqltype": "INTEGER NOT NULL", "quoted":
                    false},
            "weight": {"sqltype": "INTEGER NOT NULL", "quoted":
                       false},
            "job": {"sqltype": "VARCHAR(50)", "quoted":
                    true},
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


@fixture
def dataframe_with_datetime():
    from dateutil.parser import isoparse

    data = [{"Column": "Value_1", "at": "2020-10-01 00:00:00"},
            {"Column": "Value_2", "at": "2020-10-01 00:00:00"},
            {"Column": "Value_3", "at": "2020-10-01 00:00:00"}]
    df = pandas_dataframe(data=data)
    df['at'] = df['at'].apply(lambda x: isoparse(x))

    return df
