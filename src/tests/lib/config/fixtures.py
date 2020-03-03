from pytest import fixture


@fixture
def valid_s3_spec():
    return {
        "to": [{
            "type": "s3",
            "options": {
                "bucket": "bucket",
                "key": "key"
            }}
        ]
    }


@fixture
def invalid_s3_spec():
    return {"to": [{"type": "s3"}]}


@fixture
def valid_s3_presigned_spec():
    return {"to": [{"type": "s3-url"}]}
