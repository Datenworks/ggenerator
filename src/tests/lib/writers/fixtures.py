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
def specification():
    from os.path import abspath
    from uuid import uuid4

    absolute_path = abspath(".")
    file_name = uuid4()

    return {'uri': f"{absolute_path}/{file_name}"}
