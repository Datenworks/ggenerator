from pandas import DataFrame
from pytest import raises

from src.generators.handler import GeneratorsHandler
from src.lib.config.validator import ConfigurationValidator
from src.tests.generators.handler_fixtures import *  # noqa: F403, F401
from os import remove
import json
from src.lib.writers import writers
import pytest
<<<<<<< HEAD
import json
from os import remove
=======
>>>>>>> feature/dryrun


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
                                    'valid_specification_dataset')
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
                                    'valid_specification_dataset')
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
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = simple_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == simple_specification['size']
        for field in simple_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_argumented_specification_dataframe(self,
                                                mocker,
                                                argumented_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = argumented_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == argumented_specification['size']
        for field in argumented_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_dataframe(self, mocker, integer_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = integer_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_specification['size']
        for field in integer_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_bool_dataframe(self, mocker, bool_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = bool_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == bool_specification['size']
        for field in bool_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_char_dataframe(self, mocker, char_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = char_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == char_specification['size']
        for field in char_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_float_dataframe(self, mocker, float_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = float_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == float_specification['size']
        for field in float_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_sequence_dataframe(self,
                                        mocker,
                                        integer_sequence_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = integer_sequence_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_sequence_specification['size']
        for field in integer_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_sequence_dataframe(self,
                                          mocker,
                                          timestamp_sequence_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = timestamp_sequence_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_sequence_specification['size']
        for field in timestamp_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_string_dataframe(self, mocker, string_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = string_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == string_specification['size']
        for field in string_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_dataframe(self, mocker, timestamp_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'valid_specification_dataset')
        mock.return_value = timestamp_specification
<<<<<<< HEAD
        handler = GeneratorsHandler({"config_file": None})
        specification = handler.get_valid_specification()
=======
        handler = GeneratorsHandler({'config_file': None})
        specification = handler.valid_specification_dataset()
>>>>>>> feature/dryrun
        dataframe = handler.generate_dataframe(specification)

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_specification['size']
        for field in timestamp_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

<<<<<<< HEAD
    def test_valid_spec_handler(self, mocker, valid_specification):
        from os.path import abspath
        from uuid import uuid4

        absolute_path = abspath(".")
        file_name = uuid4()
        with open(f"{absolute_path}/{file_name}", "w") as f:
            json.dump(valid_specification, f)

        handler = \
            GeneratorsHandler({"config_file": f"{absolute_path}/{file_name}"})

        remove(f"{absolute_path}/{file_name}")
        assert handler

    def test_invalid_no_ids_spec_handler(self, mocker, no_datasets_ids):
        from os.path import abspath
        from uuid import uuid4

        absolute_path = abspath(".")
        file_name = uuid4()
        with open(f"{absolute_path}/{file_name}", "w") as f:
            json.dump(no_datasets_ids, f)

        with pytest.raises(ValueError):
            GeneratorsHandler({"config_file": f"{absolute_path}/{file_name}"})
        remove(f"{absolute_path}/{file_name}")

    def test_invalid_no_dataset_spec_handler(self, mocker,
                                             no_datasets_specification):
        from os.path import abspath
        from uuid import uuid4

        absolute_path = abspath(".")
        file_name = uuid4()
        with open(f"{absolute_path}/{file_name}", "w") as f:
            json.dump(no_datasets_specification, f)

        with pytest.raises(ValueError):
            GeneratorsHandler({"config_file": f"{absolute_path}/{file_name}"})
        remove(f"{absolute_path}/{file_name}")

    def test_invalid_no_dataset_info(self, mocker,
                                     invalid_dataset_specification):
        from os.path import abspath
        from uuid import uuid4

        absolute_path = abspath(".")
        file_name = uuid4()
        with open(f"{absolute_path}/{file_name}", "w") as f:
            json.dump(invalid_dataset_specification, f)

        with pytest.raises(ValueError):
            GeneratorsHandler({"config_file": f"{absolute_path}/{file_name}"})
        remove(f"{absolute_path}/{file_name}")
=======
    def test_generatorshandler_valid(self, valid_specification):
        with open('valid_spec.json', 'w') as f:
            json.dump(valid_specification, f)
        handler = GeneratorsHandler({'config_file': 'valid_spec.json'})
        config = handler.valid_specification_dataset()
        assert valid_specification == config
        remove('valid_spec.json')

    def test_generatorshandler_no_dataset_ids(self, invalid_no_ids_dataset):
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_ids_dataset, f)
        with pytest.raises(ValueError):
            handler = GeneratorsHandler({'config_file': 'invalid_spec.json'})
            handler.valid_specification_dataset()
        remove('invalid_spec.json')

    def test_GeneratorsHandler_no_dataset(self, no_datasets_specification):
        with open('invalid_spec.json', 'w') as f:
            json.dump(no_datasets_specification, f)
        with pytest.raises(ValueError):
            handler = GeneratorsHandler({'config_file': 'invalid_spec.json'})
            handler.valid_specification_dataset()
        remove('invalid_spec.json')

    def test_generatorshandler_no_dataset_size(self, invalid_no_size_dataset):
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_size_dataset, f)
        with pytest.raises(ValueError):
            handler = GeneratorsHandler({'config_file': 'invalid_spec.json'})
            handler.valid_specification_dataset()
        remove('invalid_spec.json')
>>>>>>> feature/dryrun
