from pytest import fixture


@fixture
def generate_files():
    yield "dset_name", "dset_format", "dset_path"


@fixture
def generators_map():
    return {
        "integer": {
            'type': "integer",
            'namespace': "basic_type",
            'generator': {
                    'optional': True,
                    'arguments': "start_at | end_at"
            }
        },
        "string": {
            'type': "string",
            'namespace': "basic_type",
            'generator': {
                    'optional': True,
                    'arguments': "length"
            }
        }
    }
