from pytest import fixture


@fixture
def valid_boolean():
    return [{
        "name": "test",
        "type": "boolean",
        "generator": {}
    }]


@fixture
def invalid_boolean():
    return [{"type": "boolean"}]


@fixture
def valid_char():
    return [{
        "name": "test",
        "type": "char",
        "generator": {}
    }]


@fixture
def invalid_char():
    return [{"type": "char"}]


@fixture
def valid_float():
    return [{
        "name": "test",
        "type": "float",
        "generator": {"start_at": 0, "end_at": 100}
    }]


@fixture
def invalid_float():
    return [{
        "name": "test",
        "type": "float",
        "generator": {"start_at": -2250738585072014e-308, "end_at": 100}
    }]


@fixture
def valid_integer():
    return [{
        "name": "test",
        "type": "integer",
        "generator": {"start_at": 0, "end_at": 100}
    }]


@fixture
def invalid_integer():
    return [{
        "name": "test",
        "type": "integer",
        "generator": {"start_at": 0, "end_at": 2147483648}
    }]


@fixture
def valid_timestamp_sequence():
    return [{
        "name": "test",
        "type": "timestamp:sequence",
        "generator": {"start_at": "2019-11-17T21:00:00"}
    }]


@fixture
def invalid_timestamp_sequence():
    return [{
        "name": "test",
        "type": "timestamp:sequence",
        "generator": {"start_at": "20/11/2019 00:00:00"}
    }]


@fixture
def valid_sequence():
    return [{
        "name": "test",
        "type": "integer:sequence",
        "generator": {"start_at": 0}
    }]


@fixture
def invalid_sequence():
    return [{
        "name": "test",
        "type": "integer:sequence",
        "generator": {"start_at": -2147483648}
    }]


@fixture
def valid_string():
    return [{
        "name": "test",
        "type": "string",
        "generator": {"length": 1}
    }]


@fixture
def invalid_string():
    return [{
        "name": "test",
        "type": "string",
        "generator": {"length": 0}
    }]


@fixture
def valid_timestamp():
    return [{
        "name": "test",
        "type": "timestamp",
        "generator": {"start_at": "2019-11-17T21:00:00",
                      "end_at": "2020-11-17T21:00:00"}
    }]


@fixture
def invalid_timestamp():
    return [{
        "name": "test",
        "type": "timestamp",
        "generator": {"start_at": "20/11/2019 00:00:00",
                      "end_at": "2020-11-17T21:00:00"}
    }]