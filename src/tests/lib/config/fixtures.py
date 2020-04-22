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
                     'type': 'pystr',
                     'generator': {
                         'length': 10
                     }},
                    {'name': 'age',
                     'type': 'pyint',
                     'generator': {
                         'start_at': 0,
                         'end_at': 120
                     }},
                    {'name': 'weight',
                     'type': 'pyfloat',
                     'generator': {
                         'start_at': 0.0,
                         'end_at': 500.0
                     }},
                    {'name': 'birth',
                     'type': 'date_between',
                     'generator': {
                         'start_date': '1980-01-01 00:00:00',
                         'end_date': '2020-01-01 00:00:00'
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
                    {'name': 'reference_id',
                     'type': 'integer:sequence',
                     'generator': {}},
                    {'name': 'level',
                     'type': 'integer',
                     'generator': {
                         'start_at': 2147483649,
                         'end_at': -2147483649
                     }},
                    {'name': 'rank',
                     'type': 'integer',
                     'generator': {
                         'start_at': 5,
                         'end_at': 4
                     }},
                    {'name': 'name',
                     'type': 'string'},
                    {'name': 'last_name',
                     'type': 'string',
                     'generator': {
                         'length': -1
                     }},
                    {'name': 'age',
                     'type': 'integer',
                     'generator': {}},
                    {'name': 'weight',
                     'type': 'float',
                     'generator': {}},
                    {'name': 'money',
                     'type': 'float',
                     'generator': {
                         'start_at': -2350738585072014e-308,
                         'end_at': 7976931348623157e+309
                     }},
                    {'name': 'taxes',
                     'type': 'float',
                     'generator': {
                         'start_at': 8.0,
                         'end_at': -1.0
                     }},
                    {'name': 'sex',
                     'type': None},
                    {'name': 'birth',
                     'type': 'timestamp'},
                    {'name': 'created_at',
                     'type': 'timestamp',
                     'generator': {
                         'start_at': 'heuheuhe',
                         'end_at': 'uheuhehu'
                     }},
                    {'name': 'updated_at',
                     'type': 'timestamp',
                     'generator': {
                         'start_at': '2020-01-01 00:00:00',
                         'end_at': '2010-01-01 00:00:00'
                     }},
                    {'name': 'hiring_at',
                     'type': 'timestamp:sequence'},
                    {'name': 'fired_at',
                     'type': 'timestamp:sequence',
                     'generator': {}},
                ],
                'format': {
                    'type': format_type
                },
                'locale': 'pt_BR',
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


@fixture
def csv_format_sample():
    return {'type': 'csv'}


@fixture
def json_format_sample():
    return {'type': 'json-array'}


@fixture
def sql_format_sample():
    return {'type': 'sql'}


@fixture
def unknown_format_sample():
    return {'type': 'unknown'}


@fixture
def file_writer_sample():
    return {'type': 'file'}


@fixture
def mysql_writer_sample():
    return {'type': 'sql',
            'options': {
                'method': 'cli',
                'engine': 'mysql'
            }}


@fixture
def postgresql_writer_sample():
    return {'type': 'sql',
            'options': {
                'method': 'cli',
                'engine': 'postgres'
            }}


@fixture
def s3_writer_sample():
    return {'type': 's3'}


@fixture
def s3_url_writer_sample():
    return {'type': 's3-url'}


@fixture
def gcs_writer_sample():
    return {'type': 'gcs'}


@fixture
def gcs_url_writer_sample():
    return {'type': 'gcs-url'}


@fixture
def unknown_writer_sample():
    return {'type': 'unknown'}


@fixture
def invalid_s3_bucket():
    return {
        "to": [{
            "type": "s3",
            "options": {
                "key": "key"
            }}
        ]
    }


@fixture
def invalid_s3_key():
    return {
        "to": [{
            "type": "s3",
            "options": {
                "bucket": "bucket"
            }}
        ]
    }


@fixture
def expected_values_rule():
    return {'items.{*}.age': {'none': False,
                              'type': str,
                              'values': ['3', '9']}}


def custom_rule_method(value):
    if value != 3:
        raise ValueError("Test value is different, expected: 3")


@fixture
def custom_rule():
    return {'items.{*}.age': {'none': False,
                              'type': str,
                              'custom': [custom_rule_method]}}
