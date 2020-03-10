import json

from mock import patch, mock_open
from pytest import raises

from src.lib.config.validator import ConfigurationValidator, \
    ConfigurationDataset
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestConfigurationValidator(object):

    def test_config_pathFinded(self, valid_spec):
        with patch("builtins.open",
                   mock_open(read_data=valid_spec)):
            validator = ConfigurationValidator("")
            config = validator.get_config()
            assert config == json.loads(valid_spec)

    def test_invalid_config(self, invalid_spec):
        with patch("builtins.open",
                   mock_open(read_data=invalid_spec)):
            validator = ConfigurationValidator("")

            with raises(ValueError):
                validator.get_config()

    def test_invalid_fields(self, invalid_spec_missing):
        myDict = invalid_spec_missing
        sample = "sample"
        size = myDict['datasets']['sample']['size']
        locale = myDict['datasets']['sample']['locale']
        fields = myDict['datasets']['sample']['fields']
        format = myDict['datasets']['sample']['format']
        serializers = myDict['datasets']['serializers']
        validator = ConfigurationDataset(
            sample,
            size,
            locale,
            fields,
            format,
            serializers)

        with raises(ValueError):
            validator.is_valid()
