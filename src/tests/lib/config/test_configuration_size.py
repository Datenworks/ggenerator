from src.lib.config.validator import ConfigurationDataset
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestValidSize(object):

    def validSize(self, valid_spec):
        myDict = valid_spec
        sample = "sample"
        size = myDict['datasets']['sample']['size']
        fields = myDict['datasets']['sample']['fields']
        format = myDict['datasets']['sample']['format']
        serializers = myDict['datasets']['serializers']
        validator = ConfigurationDataset(
            sample,
            size,
            fields,
            format,
            serializers)

        assert validator.size > 0
        assert isinstance(self.size, int)

    def invalidSize(self, invalid_spec_missing):
        myDict = invalid_spec_missing
        sample = "sample"
        size = myDict['datasets']['sample']['size']
        fields = myDict['datasets']['sample']['fields']
        format = myDict['datasets']['sample']['format']
        serializers = myDict['datasets']['serializers']
        validator = ConfigurationDataset(
            sample,
            size,
            fields,
            format,
            serializers)

        assert validator.size <= 0
