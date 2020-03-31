import json
import pytest

from mock import mock_open, patch
from os import remove
from pandas import DataFrame

from src.generators.basehandler import BaseHandler
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
        with patch('builtins.open',
                   mock_open(read_data=json.dumps(bool_specification))):
            dataset = bool_specification['datasets']['sample']
            expected_size = 10
            expected_fields = dataset['fields']

            handler = DryRunHandler({"config_file": None})
            dataframe = handler.generate_dryrun(dataset)

            assert isinstance(dataframe, DataFrame) is True
            assert dataframe.shape[0] == expected_size
            for field in expected_fields:
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

    def test_dryrunhandler_valid(self, valid_specification):
        with open('valid_spec.json', 'w') as f:
            json.dump(valid_specification, f)
        handler = DryRunHandler({'config_file': 'valid_spec.json'})
        config = handler.valid_specification_dryrun()
        assert valid_specification == config
        remove('valid_spec.json')

    def test_dryrunhandler_no_dataset_ids(self, invalid_no_ids_dataset):
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_ids_dataset, f)
        with pytest.raises(ValueError):
            handler = DryRunHandler({'config_file': 'invalid_spec.json'})
            handler.valid_specification_dryrun()
        remove('invalid_spec.json')

    def test_dryrunhandler_no_dataset(self, no_datasets_specification):
        with open('invalid_spec.json', 'w') as f:
            json.dump(no_datasets_specification, f)
        with pytest.raises(ValueError):
            handler = DryRunHandler({'config_file': 'invalid_spec.json'})
            handler.valid_specification_dryrun()
        remove('invalid_spec.json')

    def test_dryrunhandler_no_dataset_size(self, invalid_no_size_dataset):
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_size_dataset, f)
        with pytest.raises(ValueError):
            handler = DryRunHandler({'config_file': 'invalid_spec.json'})
            handler.valid_specification_dryrun()
        remove('invalid_spec.json')

    def test_output(self, valid_dryrun, valid_specification):
        with open('valid_spec.json', 'w') as f:
            json.dump(valid_specification, f)
        handler = BaseHandler()
        dry = DryRunHandler({'config_file': 'valid_spec.json'})
        dataframe = handler.generate_dataframe(valid_dryrun, 10)
        key = "sample"
        dataset_fields = valid_dryrun['fields']
        assert dry.print_dryrun(dataframe, key, dataset_fields) is None
        remove('valid_spec.json')

    def test_generate_dryrun(self, mocker, valid_specification):
        mock_config = mocker.patch \
                            .object(DryRunHandler,
                                    'valid_specification_dryrun')
        mock_config.return_value = valid_specification

        handler = DryRunHandler(arguments={'config_file': None})
        assert handler.generate() is None
