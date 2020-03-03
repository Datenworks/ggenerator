from pandas import DataFrame
from pytest import raises

from src.generators.handler import GeneratorsHandler
from src.lib.config.validator import ConfigurationValidator
from src.tests.generators.handler_fixtures import *  # noqa: F403, F401
from src.lib.writers import writers


class TestGeneratorsHandler(object):
    """Unit-test of GeneratorsHandler class"""

    def test_valid_specification(self, mocker, valid_specification):
        mock = mocker.patch \
                     .object(ConfigurationValidator, 'get_config')
        mock.return_value = valid_specification

        GeneratorsHandler(arguments={'config_file': None})

        mock.assert_called()

    def test_without_dataset(self, mocker, no_datasets_specification):
        mock = mocker.patch \
                     .object(ConfigurationValidator, 'get_config')
        mock.return_value = no_datasets_specification

        with raises(ValueError):
            GeneratorsHandler(arguments={'config_file': None})

            mock.assert_called()

    def test_invalid_dataset(self, mocker, invalid_dataset_specification):
        mock = mocker.patch \
                     .object(ConfigurationValidator, 'get_config')
        mock.return_value = invalid_dataset_specification

        with raises(ValueError):
            GeneratorsHandler(arguments={'config_file': None})

            mock.assert_called()

    def test_generate(self, mocker, valid_specification):
        mock_write = mocker.patch \
                           .object(GeneratorsHandler, 'write_dataframe')
        mock_write.return_value = 'file_path'
        mock_config = mocker.patch \
                            .object(GeneratorsHandler,
                                    'get_valid_specification')
        mock_config.return_value = valid_specification

        handler = GeneratorsHandler(arguments={'config_file': None})
        for key, format_, path in handler.generate():
            assert key is not None
            assert isinstance(key, str)
            assert format_ is not None
            assert isinstance(format_, str)
            assert path is not None
            assert isinstance(path, str)

        mock_write.assert_called()

    def test_write(self, mocker, valid_specification):
        mock_config = mocker.patch \
                            .object(GeneratorsHandler,
                                    'get_valid_specification')
        mock_config.return_value = valid_specification

        handler = GeneratorsHandler(arguments={'config_file': None})
        for key in valid_specification['datasets'].keys():
            dataset = valid_specification['datasets'][key]
            dataset_format = dataset['format']
            dataframe = handler.generate_dataframe(dataset)
            for destination in dataset['serializers']['to']:
                file_type = destination['type']
                writer = writers[file_type]
                mock = mocker.patch.object(writer, 'write')
                mock.return_value = 'file_path'
                file_path = handler.write_dataframe(dataframe=dataframe,
                                                    destination=destination,
                                                    format_=dataset_format)

                mock.assert_called()
                assert file_path == 'file_path'

    def test_simple_specification_dataframe(self,
                                            mocker,
                                            simple_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = simple_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

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
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == argumented_specification['size']
        for field in argumented_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_dataframe(self, mocker, integer_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = integer_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_specification['size']
        for field in integer_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_bool_dataframe(self, mocker, bool_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = bool_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == bool_specification['size']
        for field in bool_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_char_dataframe(self, mocker, char_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = char_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == char_specification['size']
        for field in char_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_float_dataframe(self, mocker, float_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = float_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

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
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

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
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_sequence_specification['size']
        for field in timestamp_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_string_dataframe(self, mocker, string_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = string_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == string_specification['size']
        for field in string_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_dataframe(self, mocker, timestamp_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = timestamp_specification
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.get_valid_specification()
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_specification['size']
        for field in timestamp_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']
