from pytest import fixture


@fixture
def simple_specification():
    return {'size': 100,
            'fields': [{'name': 'id',
                        'type': 'integer:sequence',
                        'generator': {},
                        'expected': 'int64'},
                       {'name': 'text',
                        'type': 'string',
                        'generator': {},
                        'expected': 'object'}]}


@fixture
def argumented_specification():
    return {'size': 200,
            'fields': [{'name': 'id',
                        'type': 'integer:sequence',
                        'generator': {'start_at': 10,
                                      'step': 2},
                        'expected': 'int64'},
                       {'name': 'date',
                        'type': 'timestamp',
                        'generator': {'start_at': "2000-01-01T00:00:00Z",
                                      'end_at':  '2019-12-31T01:00:00Z'},
                        'expected': 'datetime64[ns]'}]}


def sample(type, expected):
    return {'size': 200,
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {},
                        'expected': expected}]}


def sample_timestamp(type, expected):
    return {'size': 200,
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {
                            'start_at': '2019-01-01T01:00:00Z',
                            'end_at':  '2019-12-31T01:00:00Z'
                        },
                        'expected': expected}]}


def sample_timestamp_sequence(type, expected):
    return {'size': 200,
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {
                            'start_at': '2019-01-01T01:00:00Z'
                            },
                        'expected': expected}]}


@fixture
def integer_specification():
    return sample('integer', 'int64')


@fixture
def bool_specification():
    return sample('boolean', 'bool')


@fixture
def char_specification():
    return sample('char', 'object')


@fixture
def float_specification():
    return sample('float', 'float64')


@fixture
def timestamp_sequence_specification():
    return sample_timestamp_sequence('timestamp:sequence', 'datetime64[ns]')


@fixture
def integer_sequence_specification():
    return sample('integer:sequence', 'int64')


@fixture
def string_specification():
    return sample('string', 'object')


@fixture
def timestamp_specification():
    return sample_timestamp('timestamp', 'datetime64[ns]')


@fixture
def valid_spec():
    return {
        "datasets": {
            "$id": {
                "size": 1000,
                "fields": [{
                    "name": "id",
                    "type": "integer:sequence",
                    "generator": {
                        "start_at": 0
                    }
                }],
                "format": {
                    "type": "csv",
                    "options": {
                        "header": True,
                        "sep": ","
                    }
                },
                "serializers": {
                    "to": [{
                            "type": "file",
                            "uri": "myfile.csv"
                        }
                    ]
                }
            }
        }
    }


@fixture
def invalid_spec_no_ids():
    return {
        "datasets": {}
    }


@fixture
def invalid_spec_no_dataset():
    return {}


@fixture
def invalid_spec_no_infos_dataset():
    return {
        "datasets": {
            "$id": {
                "size": 10,
                "fields": [],
                "format": {},
                "serializers": {}
            }
        }
    }
