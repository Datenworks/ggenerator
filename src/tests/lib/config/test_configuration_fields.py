from src.lib.config.validator import ConfigurationFields


class TestConfigurationFormat(object):

    def test_fields_format(self):
        format_sample = [{
            "name": "id",
            "type": ":integer:sequence",
            "generator": {}
        }]
        validator = ConfigurationFields(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_fields_id_format(self):
        format_sample = [{
            "type": "sequence",
            "generator": {}
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
            "type": "sequence",
        }]
        validator = ConfigurationFields(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False
