import json
import pytest

from mock import mock_open, patch
from os import remove
from pandas import DataFrame

from src.generators.handler import BaseHandler
from src.tests.generators.handler_fixtures import *  # noqa: F403, F401


class TestBaseHundler(object):

    def test_simple_specification_dataframe(self,
                                            mocker,
                                            simple_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = simple_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(specification,
                                               simple_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == simple_specification['size']
        for field in simple_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_argumented_specification_dataframe(self,
                                                mocker,
                                                argumented_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = argumented_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(
            specification,
            argumented_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == argumented_specification['size']
        for field in argumented_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_dataframe(self, mocker, integer_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = integer_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(specification,
                                               integer_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_specification['size']
        for field in integer_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_bool_dataframe(self, mocker, bool_specification):
        with patch('builtins.open',
                   mock_open(read_data=json.dumps(bool_specification))):
            dataset = bool_specification['datasets']['sample']
            expected_size = dataset['size']
            expected_fields = dataset['fields']

            handler = BaseHandler()
            dataframe = handler.generate_dataframe(dataset, dataset['size'])

            assert isinstance(dataframe, DataFrame) is True
            assert dataframe.shape[0] == expected_size
            for field in expected_fields:
                assert dataframe[field['name']].dtype.name == field['expected']

    def test_char_dataframe(self, mocker, char_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = char_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(specification,
                                               char_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == char_specification['size']
        for field in char_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_float_dataframe(self, mocker, float_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = float_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(specification,
                                               float_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == float_specification['size']
        for field in float_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_integer_sequence_dataframe(self,
                                        mocker,
                                        integer_sequence_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = integer_sequence_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(
            specification,
            integer_sequence_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == integer_sequence_specification['size']
        for field in integer_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_sequence_dataframe(self,
                                          mocker,
                                          timestamp_sequence_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = timestamp_sequence_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(
            specification,
            timestamp_sequence_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_sequence_specification['size']
        for field in timestamp_sequence_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_string_dataframe(self, mocker, string_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = string_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(specification,
                                               string_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == string_specification['size']
        for field in string_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_timestamp_dataframe(self, mocker, timestamp_specification):
        mock = mocker.patch \
                     .object(BaseHandler, 'valid_specification')
        mock.return_value = timestamp_specification
        handler = BaseHandler()
        specification = handler.valid_specification()
        dataframe = handler.generate_dataframe(specification,
                                               timestamp_specification['size'])

        assert isinstance(dataframe, DataFrame) is True
        assert dataframe.shape[0] == timestamp_specification['size']
        for field in timestamp_specification['fields']:
            assert dataframe[field['name']].dtype.name == field['expected']

    def test_basehandler_valid(self, valid_specification):
        handler = BaseHandler()

        with open('valid_spec.json', 'w') as f:
            json.dump(valid_specification, f)

        config = handler.valid_specification('valid_spec.json')

        assert valid_specification == config

        remove('valid_spec.json')

    def test_basehandler_no_dataset(self, no_datasets_specification):
        handler = BaseHandler()
        with open('invalid_spec.json', 'w') as f:
            json.dump(no_datasets_specification, f)

        with pytest.raises(ValueError):
            handler.valid_specification('invalid_spec.json')
        remove('invalid_spec.json')

    def test_basehandler_no_dataset_ids(self, invalid_no_ids_dataset):
        handler = BaseHandler()
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_ids_dataset, f)

        with pytest.raises(ValueError):
            handler.valid_specification('invalid_spec.json')
        remove('invalid_spec.json')

    def test_basehandler_no_dataset_size(self, invalid_no_size_dataset):
        handler = BaseHandler()
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_size_dataset, f)

        with pytest.raises(ValueError):
            handler.valid_specification('invalid_spec.json')
        remove('invalid_spec.json')

    def test_basehandler_no_dataset_locale(self, invalid_no_locale_dataset):
        handler = BaseHandler()
        with open('invalid_spec.json', 'w') as f:
            json.dump(invalid_no_locale_dataset, f)

        with pytest.raises(ValueError):
            handler.valid_specification('invalid_spec.json')
        remove('invalid_spec.json')

    def test_date_format_invalid_specification(self,
                                               mocker,
                                               invalid_dateformat):
        with patch('builtins.open',
                   mock_open(read_data=json.dumps(invalid_dateformat))):
            handler = BaseHandler()
            with pytest.raises(ValueError):
                handler.valid_specification('')

    def test_malformed_json(self, mocker, malformed_json):
        with patch('builtins.open',
                   mock_open(read_data=malformed_json)):
            handler = BaseHandler()
            with pytest.raises(ValueError):
                handler.valid_specification('')

    def test_unknown_type(self, mocker, unknown_type_spec):
        with patch('builtins.open',
                   mock_open(read_data=json.dumps(unknown_type_spec))):
            handler = BaseHandler()
            with pytest.raises(ValueError):
                handler.valid_specification('')

    def test_basehandler_valid_replace(self, valid_spec_for_replace_rules):
        handler = BaseHandler()

        with open('valid_spec_for_replace_rules.json', 'w') as f:
            json.dump(valid_spec_for_replace_rules, f)

        config = handler.valid_specification(
            'valid_spec_for_replace_rules.json')

        assert valid_spec_for_replace_rules == config

        remove('valid_spec_for_replace_rules.json')

    def test_basehandler_invalid_replace_without_schema(
                self,
                invalid_spec_for_replace_rules_without_schema):
        handler = BaseHandler()

        with open(
             'invalid_spec_for_replace_rules_without_schema.json', 'w') as f:
            json.dump(invalid_spec_for_replace_rules_without_schema, f)
        with pytest.raises(ValueError):
            handler.valid_specification(
             'invalid_spec_for_replace_rules_without_schema.json')

        remove('invalid_spec_for_replace_rules_without_schema.json')

    def test_basehandler_invalid_replace_without_sqltype(
                self,
                invalid_spec_for_replace_rules_without_sqltype):
        handler = BaseHandler()

        with open(
             'invalid_spec_for_replace_rules_without_sqltype.json', 'w') as f:
            json.dump(invalid_spec_for_replace_rules_without_sqltype, f)
        with pytest.raises(ValueError):
            handler.valid_specification(
             'invalid_spec_for_replace_rules_without_sqltype.json')

        remove('invalid_spec_for_replace_rules_without_sqltype.json')
