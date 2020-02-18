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
                        'generator': {'start_at': "2000-01-01T00:00:00UTC"},
                        'expected': 'datetime64[ns]'}]}


def sample(type, expected):
    return {'size': 200,
            'fields': [{'name': 'id',
                        'type': type,
                        'generator': {},
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
