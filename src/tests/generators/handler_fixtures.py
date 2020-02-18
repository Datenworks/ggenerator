from pytest import fixture


@fixture
def simple_valid_specification():
    return {'size': 100,
            'fields': [{'name': 'id',
                        'type': 'integer:sequence',
                        'generator': {}},
                       {'name': 'text',
                        'type': 'string',
                        'generator': {}}]}
