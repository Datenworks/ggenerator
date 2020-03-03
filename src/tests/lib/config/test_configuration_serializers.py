from src.lib.config.validator import ConfigurationSerializer
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestConfigurationSerializers(object):

    def test_valid_to(self):
        format_sample = {"to": [{"type": "file", "uri": ""}]}
        validator = ConfigurationSerializer(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_valid_s3(self, valid_s3_spec):
        validator = ConfigurationSerializer(valid_s3_spec)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_s3(self, invalid_s3_spec):
        validator = ConfigurationSerializer(invalid_s3_spec)
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_s3_presigned_url(self, valid_s3_presigned_spec):
        validator = ConfigurationSerializer(valid_s3_presigned_spec)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_to(self):
        format_sample = {"to": [{}]}
        validator = ConfigurationSerializer(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False
