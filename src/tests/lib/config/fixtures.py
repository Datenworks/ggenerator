from pytest import fixture


def valid_specfication(format_type):
    return {
        'datasets': {
            'valid': {
                'fields': [
                    {'name': 'id',
                     'type': 'integer:sequence',
                     'generator': {
                         'start_at': 0
                     }},
                    {'name': 'name',
                     'type': 'string',
                     'generator': {
                         'length': 10
                     }},
                    {'name': 'age',
                     'type': 'integer',
                     'generator': {
                         'start_at': 0,
                         'end_at': 120
                     }},
                    {'name': 'weight',
                     'type': 'float',
                     'generator': {
                         'start_at': 0.0,
                         'end_at': 500.0
                     }},
                    {'name': 'sex',
                     'type': 'char'},
                    {'name': 'birth',
                     'type': 'timestamp',
                     'generator': {
                         'start_at': '1980-01-01 00:00:00',
                         'end_at': '2020-01-01 00:00:00'
                     }},
                    {'name': 'hiring_at',
                     'type': 'timestamp:sequence',
                     'generator': {
                         'start_at': '1980-01-01 00:00:00'
                     }},
                ],
                'format': {
                    'type': format_type
                },
                'locale': 'pt_BR',
                'serializers': {
                    'to': [
                        {
                            'type': 'file',
                            'uri': ''
                        }
                    ]
                },
                'size': 100
            }
        }
    }


def invalid_specfication(format_type):
    return {
        'datasets': {
            'invalid': {
                'fields': [
                    {'name': 'id',
                     'type': 'integer:sequence'},
                    {'name': 'name',
                     'type': 'string'},
                    {'name': 'age',
                     'type': 'integer',
                     'generator': {}},
                    {'name': 'weight',
                     'type': 'float',
                     'generator': {}},
                    {'name': 'sex',
                     'type': 'char'},
                    {'name': 'birth',
                     'type': 'timestamp'},
                    {'name': 'opa',
                     'type': 'timestamp',
                     'generator': {
                         'start_at': 'heuheuhe',
                         'end_at': 'uheuhehu'
                     }},
                    {'name': 'hiring_at',
                     'type': 'timestamp:sequence'},
                ],
                'format': {
                    'type': format_type
                },
                'serializers': {
                    'to': []
                },
                'size': '100'
            }
        }
    }


@fixture
def valid_csv_specification():
    return valid_specfication('csv')


@fixture
def valid_json_specification():
    return valid_specfication('json')


@fixture
def invalid_csv_specification():
    return invalid_specfication('csv')


@fixture
def invalid_json_specification():
    return invalid_specfication('json')


@fixture
def str_type_rule():
    return {'item': {'none': False, 'type': str}}


@fixture
def dict_type_rule():
    return {'item': {'none': False, 'type': dict}}


@fixture
def invalid_type_sample():
    return {'item': 15}


@fixture
def fixed_index_rule():
    return {'items.[1].age': {'none': False, 'type': int}}


@fixture
def collection_sample():
    return {'items': [{'age': '5'}, {'age': '7'}, {'age': '15'}]}


@fixture
def fixed_key_rule():
    return {'items.{second}.age': {'none': False, 'type': int}}


@fixture
def dictionary_sample():
    return {
        'items': {
            'first': {'age': '5'},
            'second': {'age': '7'},
            'third': {'age': '15'}
        }
    }
