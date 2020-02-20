from src.lib.config.validator import ConfigurationSerializer


class TestConfigurationSerializers(object):

    def test_valid_to(self):
        format_sample = {
            "to": [{
                "type": "file",
                "uri": ""
            }
            ]
        }
        validator = ConfigurationSerializer(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is True

    def test_invalid_to(self):
        format_sample = {
            "to": [{

            }]
        }
        validator = ConfigurationSerializer(format_sample)
        is_valid = validator.is_valid()
        assert is_valid is False
