from src.lib.config.validator import ConfigurationFormat


class TestConfigurationFormat(object):

    def test_csv_valid_format(self):
        format_sample = {
            "type": "csv",
            "header": True
        }
        validator = ConfigurationFormat(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_json_valid_format(self):
        format_sample = {
            "type": "json",
            "header": True
        }
        validator = ConfigurationFormat(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_witout_type_format(self):
        format_sample = {"header": True}
        validator = ConfigurationFormat(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_without_header_format(self):
        format_sample = {"type": "csv"}
        validator = ConfigurationFormat(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True
