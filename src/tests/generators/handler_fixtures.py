from pytest import fixture


@fixture
def simple_specification():
    return {'size': 100,
            'locale': 'pt_BR',
            'fields': [{'name': 'id',
                        'type': 'integer:sequence',
                        'generator': {},
                        'expected': 'int64'},
                       {'name': 'text',
                        'type': 'pystr',
                        'generator': {},
                        'expected': 'object'}]}


@fixture
def argumented_specification():
    return {'size': 200,
            'locale': 'pt_BR',
            'fields': [{'name': 'id',
                        'type': 'integer:sequence',
                        'generator': {'start_at': 10,
                                      'step': 2},
                        'expected': 'int64'},
                       {'name': 'date',
                        'type': 'date_time_between',
                        'generator': {'start_date': "-10d",
                                      'end_date':  '+1y'},
                        'expected': 'datetime64[ns]'}]}


def sample(type, expected):
    return {'size': 200,
            'locale': 'pt_BR',
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {},
                        'expected': expected}]}


def dataframe_sample(type, expected):
    return {
        'datasets': {
            'sample': {
                'size': 200,
                'locale': 'pt_BR',
                'fields': [
                    {
                        'name': 'id',
                        'type': type,
                        'generator': {},
                        'expected': expected
                    }
                ],
                'format': {'type': 'csv'},
                'serializers': {
                    'to': [
                        {
                            'type': 'file',
                            'uri': ''
                        }
                    ]
                }
            }
        }
    }


def sample_timestamp(type, expected):
    return {'size': 200,
            'locale': 'pt_BR',
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {
                            'start_date': '-1d',
                            'end_date':  '+1d'
                        },
                        'expected': expected}]}


def sample_timestamp_sequence(type, expected):
    return {'size': 200,
            'locale': 'pt_BR',
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {
                            'start_at': '2019-01-01T01:00:00Z'
                        },
                        'expected': expected}]}


@fixture
def integer_specification():
    return sample('pyint', 'int64')


@fixture
def bool_specification():
    return dataframe_sample('boolean', 'bool')


@fixture
def char_specification():
    return sample('pystr', 'object')


@fixture
def name_specification():
    return sample('name', 'object')


@fixture
def float_specification():
    return sample('pyfloat', 'float64')


@fixture
def timestamp_sequence_specification():
    return sample_timestamp_sequence('timestamp:sequence', 'datetime64[ns]')


@fixture
def integer_sequence_specification():
    return sample('integer:sequence', 'int64')


@fixture
def string_specification():
    return sample('pystr', 'object')


@fixture
def timestamp_specification():
    return sample_timestamp('date_time_between', 'datetime64[ns]')


@fixture
def valid_specification():
    return {
        "datasets": {
            "teste3": {
                "fields": [
                    {
                        "type": "integer:sequence",
                        "name": "id",
                        "generator": {
                            "start_at": 1
                        }
                    }
                ],
                "size": 100,
                "locale": "pt_BR",
                "format": {
                    "type": "csv"
                },
                "serializers": {
                    "to": [
                        {
                            "type": "file",
                            "uri": "/tmp/teste.csv"
                        }
                    ]
                }
            }
        }
    }


@fixture
def no_datasets_specification():
    return {}


@fixture
def invalid_no_ids_dataset():
    return {"datasets": {}}


@fixture
def invalid_no_size_dataset():
    return {"datasets": {
        "$id": {
            "fields": [],
            "locale": "",
            "format": {},
            "serializers": {}
        }
    }
    }


@fixture
def invalid_no_locale_dataset():
    return {"datasets": {
        "$id": {
            "fields": [],
            "size": 10,
            "format": {},
            "serializers": {}
        }
    }
    }


@fixture
def invalid_no_size_dryrun():
    return {"datasets": {
        "$id": {
            "fields": [],
            "format": {},
            "serializers": {}
        }
    }
    }


@fixture
def invalid_dataset_specification():
    return {"datasets": {
        "teste3": {
            "fields": [{"type": "integer:sequence",
                                "name": "id",
                                "generator": {"start_at": 1}}],
            "size": "",
                    "locale": "pt_BR",
                    "format": {"type": "csv"},
                    "serializers": {
                        "to": [{"type": "file",
                                "uri": "/tmp/teste.csv"}]}}}}


@fixture
def valid_dryrun():
    return {"size": 10,
            "locale": "pt_BR",
            "fields": [{
                "name": "code",
                "type": "integer:sequence",
                "generator": {"start_at": 10}
            }]
            }
