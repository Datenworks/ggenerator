from pandas import DataFrame

from src.generators.handler import GeneratorsHandler
from src.tests.generators.handler_fixtures import simple_specification, \
    argumented_specification, integer_specification, bool_specification, \
    char_specification, float_specification, string_specification, \
    integer_sequence_specification, timestamp_sequence_specification, \
    timestamp_specification


class TestGeneratorsHandler(object):
    """Unit-test of GeneratorsHandler class"""

    def test_simple_specification_dataframe(self,
                                            mocker,
                                            simple_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = simple_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == simple_specification['size']
        for field in simple_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_argumented_specification_dataframe(self,
                                                mocker,
                                                argumented_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = argumented_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == argumented_specification['size']
        for field in argumented_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_dataframe(self, mocker, integer_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = integer_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_specification['size']
        for field in integer_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_bool_dataframe(self, mocker, bool_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = bool_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == bool_specification['size']
        for field in bool_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_char_dataframe(self, mocker, char_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = char_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == char_specification['size']
        for field in char_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_float_dataframe(self, mocker, float_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = float_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == float_specification['size']
        for field in float_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_sequence_dataframe(self,
                                        mocker,
                                        integer_sequence_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = integer_sequence_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_sequence_specification['size']
        for field in integer_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_sequence_dataframe(self,
                                          mocker,
                                          timestamp_sequence_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = timestamp_sequence_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_sequence_specification['size']
        for field in timestamp_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_string_dataframe(self, mocker, string_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = string_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == string_specification['size']
        for field in string_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_dataframe(self, mocker, timestamp_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = timestamp_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_specification['size']
        for field in timestamp_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']