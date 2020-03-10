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


@fixture
def valid_spec():
    import json

    return json.dumps({
        "datasets": {
            "sample": {
                "size": 10,
                "fields": [
                    {
                        "name": "code",
                        "type": "integer:sequence",
                        "generator": {"start_at": 10}
                    },
                    {
                        "name": "date",
                        "type": "timestamp",
                        "generator": {
                            "start_at":
                            "1994-02-20T15:48:33-03:00",
                            "end_at": "2012-07-31T19:55:00-03:00"}
                    },
                    {
                        "name": "description",
                        "type": "string",
                        "generator": {"length": 15}
                    }
                ],
                "format": {
                    "type": "csv",
                    "options": {
                        "header": False,
                        "sep": ","
                    }
                },
                "serializers": {
                    "to": [
                        {
                            "type": "file",
                            "uri": "/home/tadeu/dataset.csv"
                        },
                        {
                            "type": "file",
                            "uri": "/home/tadeu/Documents/anothe_dataset.csv"
                        }
                    ]
                }
            }
        }
    })


@fixture
def invalid_spec():
    return ""


@fixture
def invalid_spec_missing():

    dict1 = {"datasets": {
        "sample": {
            "locale": "",
            "size": '-1',
            "fields": [

            ],
            "format": {

            }
        },
        "serializers": {

        }
    }
    }
    return dict1
