from pytest import fixture


def pandas_dataframe(data):
    from pandas import DataFrame

    dataframe = DataFrame(data=data)

    return dataframe


@fixture
def pandas_dataframe_with_data():
    data = [{"Column": "Value_1", "Column2": "Value2_1"},
            {"Column": "Value_2", "Column2": "Value2_2"},
            {"Column": "Value_3", "Column2": "Value2_3"}]
    return pandas_dataframe(data=data)


@fixture
def pandas_dataframe_without_data():
    return pandas_dataframe(data=[])


@fixture
def specification_s3():
    from uuid import uuid4

    file_name = uuid4().hex

    return {
        'type': 's3',
        'options': {
            'bucket': 'mybucket',
            'key': file_name
        }
    }


@fixture
def specification_gcs():
    from uuid import uuid4

    file_name = uuid4().hex

    return {
        'type': 'gcs',
        'options': {
            'bucket': 'mybucket',
            'key': file_name
        }
    }


@fixture
def specification_azure_bs():
    from uuid import uuid4

    file_name = uuid4().hex

    return {
        'type': 'azure-bs',
        'options': {
            'container': 'mycontainer',
            'blob': file_name
        }
    }


@fixture
def specification_with_url():
    return {
        'type': 's3-url',
        'options': {
            "path": "file/path/example.json"
        }
    }


@fixture
def specification_url_gcs():
    return {
        'type': 'gcs-url',
        'uri': 'https://signed-url.example.com'
    }


@fixture
def specification_without_url():
    return {'type': 's3-url'}


@fixture
def gcs_without_url():
    return {'type': 's3-url'}


@fixture
def signed_post_file():
    return '{"url": "s3.url.com", "fields": {}}'


@fixture
def s3_without_options():
    return {
        'type': 's3'
    }


@fixture
def s3_without_bucket():
    return {
        "type": "s3",
        "options": {
            "key": "/path/to/file.json"
        }
    }
