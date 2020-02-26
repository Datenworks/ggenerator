from src.lib.config.validator import ConfigurationFields
from src.tests.lib.config.configuration_fields_fixtures import valid_boolean, \
    invalid_boolean, valid_char, invalid_char, valid_float, invalid_float, \
    valid_integer, invalid_integer, valid_timestamp_sequence, \
    invalid_timestamp_sequence, valid_sequence, invalid_sequence, \
    valid_string, invalid_string, valid_timestamp, invalid_timestamp


class TestConfigurationFormat(object):

    def test_fields_format(self):
        format_sample = [{
            "name": "id",
            "type": "integer:sequence",
            "generator": {"start_at": 0}
        }]
        validator = ConfigurationFields(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_fields_id_format(self):
        format_sample = [{
            "type": "timestamp:sequence",
            "generator": {
                "start_at": "2019-01-01T00:00:00UTC"
            }
        }]
        validator = ConfigurationFields(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_fields_type_format(self):
        format_sample = [{
            "name": "id",
            "generator": {}
        }]
        validator = ConfigurationFields(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_fields_generator_format(self):
        format_sample = [{
            "name": "id",
            "type": "integer:sequence",
            "generator":{
                "asdasd": "asdasd"
            }
        }]
        validator = ConfigurationFields(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_boolean(self, valid_boolean):
        validator = ConfigurationFields(valid_boolean)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_boolean(self, invalid_boolean):
        validator = ConfigurationFields(invalid_boolean)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_char(self, valid_char):
        validator = ConfigurationFields(valid_char)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_char(self, invalid_char):
        validator = ConfigurationFields(invalid_char)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_float(self, valid_float):
        validator = ConfigurationFields(valid_float)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_float(self, invalid_float):
        validator = ConfigurationFields(invalid_float)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_integer(self, valid_integer):
        validator = ConfigurationFields(valid_integer)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_integer(self, invalid_integer):
        validator = ConfigurationFields(invalid_integer)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_timestamp_sequence(self, valid_timestamp_sequence):
        validator = ConfigurationFields(valid_timestamp_sequence)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_timestamp_sequence(self, invalid_timestamp_sequence):
        validator = ConfigurationFields(invalid_timestamp_sequence)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_sequence(self, valid_sequence):
        validator = ConfigurationFields(valid_sequence)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_sequence(self, invalid_sequence):
        validator = ConfigurationFields(invalid_sequence)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_string(self, valid_string):
        validator = ConfigurationFields(valid_string)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_string(self, invalid_string):
        validator = ConfigurationFields(invalid_string)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_timestamp(self, valid_timestamp):
        validator = ConfigurationFields(valid_timestamp)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_timestamp(self, invalid_timestamp):
        validator = ConfigurationFields(invalid_timestamp)
        is_valid = validator.is_valid()
        assert is_valid is False
