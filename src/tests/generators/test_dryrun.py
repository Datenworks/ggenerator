from pandas import DataFrame

from src.generators.dryrunhandler import DryRunHandler
from src.tests.generators.handler_fixtures import *  # noqa: F403, F401


class TestDryRunHandler(object):
    """Unit-test of DryRunHandler class"""

    def test_simple_specification_dataframe(self,
                                            mocker,
                                            simple_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = simple_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in simple_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_argumented_specification_dataframe(self,
                                                mocker,
                                                argumented_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = argumented_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in argumented_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_dataframe(self, mocker, integer_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = integer_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in integer_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_bool_dataframe(self, mocker, bool_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = bool_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in bool_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_char_dataframe(self, mocker, char_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = char_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in char_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_float_dataframe(self, mocker, float_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = float_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in float_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_sequence_dataframe(self,
                                        mocker,
                                        integer_sequence_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = integer_sequence_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in integer_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_sequence_dataframe(self,
                                          mocker,
                                          timestamp_sequence_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = timestamp_sequence_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in timestamp_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_string_dataframe(self, mocker, string_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = string_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in string_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_dataframe(self, mocker, timestamp_specification):
        mock = mocker.patch \
                     .object(DryRunHandler, 'valid_specification_dryrun')
        mock.return_value = timestamp_specification
        handler = DryRunHandler({'config_file': None})
        specification = handler.valid_specification_dryrun()
        dataframe = handler.generate_dryrun(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == 10
        for field in timestamp_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_output(self):
        pass
