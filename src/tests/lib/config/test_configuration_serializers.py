from src.lib.config.validator import ConfigurationSerializer
import pytest
import click
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestConfigurationSerializers(object):

    def test_valid_to(self, mocker):
        format_sample = {
            "to": [{
                "type": "file",
                "uri": ""
            }
            ]
        }
        mock = mocker.patch.object(click, 'prompt')
        mock.return_value = "https://onevalidurl"

        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_valid_s3(self, valid_s3_spec):
        validator = ConfigurationSerializer(valid_s3_spec, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_s3(self, invalid_s3_spec):
        validator = ConfigurationSerializer(invalid_s3_spec, 'id')
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_to_gcs(self):
        format_sample = {
            "to": [{
                "type": "gcs",
                "options": {
                    "bucket": "abcde",
                    "key": "path/to/file"
                    }
                }
            ]
        }
        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_to_gcs(self):
        format_sample = {
            "to": [{
                "type": "gcs",
                "options": {
                    }
                }
            ]
        }
        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_valid_to_s3_url(self):
        format_sample = {
            "to": [{
                "type": "s3-url",
                "uri": "https://path/to/file.csv"
            }
            ]
        }
        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_valid_to_s3_without_url_user_input(self, mocker):
        format_sample = {
            "to": [{
                "type": "s3-url"
                }
            ]
        }
        mock = mocker.patch.object(click, 'prompt')
        mock.return_value = "https://onevalidurl"

        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_valid_to_gcp_url(self):
        format_sample = {
            "to": [{
                "type": "gcs-url",
                "uri": "https://path/to/file.csv"
            }
            ]
        }
        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_valid_to_gcp_without_url_user_input(self, mocker):
        format_sample = {
            "to": [{
                "type": "gcs-url"
                }
            ]
        }
        mock = mocker.patch.object(click, 'prompt')
        mock.return_value = "https://onevalidurl"

        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_valid_to_gcs_invalid_url(self):
        format_sample = {
            "to": [{
                "type": "gcs-url",
                "uri": "sdfsdfsdf"
                }
            ]
        }
        validator = ConfigurationSerializer(format_sample, 'id')
        is_valid = validator.is_valid()
        assert is_valid is False

    def test_invalid_to(self):
        format_sample = {"to": [{}]}
        validator = ConfigurationSerializer(format_sample, 'id')

        with pytest.raises(Exception):
            validator.is_valid()
