from pytest import fixture


def pandas_dataframe(data):
    from pandas import DataFrame

    dataframe = DataFrame(data=data)

    return dataframe


@fixture
def pandas_dataframe_with_data():
    data = [{"Column": "Value_1"},
            {"Column": "Value_2"},
            {"Column": "Value_3"}]
    return pandas_dataframe(data=data)


@fixture
def pandas_dataframe_without_data():
    return pandas_dataframe(data=[])


@fixture
def schema_quoted_error():
    quoted = {"schema": {
                "field": {"quoted": "oi"}}}
    return quoted


@fixture
def schema_sqltype_error():
    sqltype = {"mode": "replace",
               "schema": {
                "field": {"sqltype": 23, "quoted": True}}}
    return sqltype
