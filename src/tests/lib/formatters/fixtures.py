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
def dataframe_with_datetime():
    from dateutil.parser import isoparse

    data = [{"Column": "Value_1", "at": "2020-10-01 00:00:00"},
            {"Column": "Value_2", "at": "2020-10-01 00:00:00"},
            {"Column": "Value_3", "at": "2020-10-01 00:00:00"}]
    df = pandas_dataframe(data=data)
    df['at'] = df['at'].apply(lambda x: isoparse(x))

    return df
