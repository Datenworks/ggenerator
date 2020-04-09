from pytest import raises

from src.lib.config import general_rules
from src.lib.config.inspector import ConfigurationInpector
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestConfigurationInspector(object):
    """Unit-test of TestConfigurationInspector class"""

    def test_valid_csv_configuration(self, valid_csv_specification):
        inspector = ConfigurationInpector()
        inspect = inspector. \
            inspect_rules(rules=general_rules,
                          configuration=valid_csv_specification)
        assert inspect is None

    def test_valid_json_configuration(self, valid_json_specification):
        inspector = ConfigurationInpector()
        inspect = inspector. \
            inspect_rules(rules=general_rules,
                          configuration=valid_json_specification)
        assert inspect is None

    def test_invalid_csv_configuration(self, invalid_csv_specification):
        inspector = ConfigurationInpector()
        with raises(ValueError):
            inspector.inspect_rules(rules=general_rules,
                                    configuration=invalid_csv_specification)

    def test_invalid_json_configuration(self, invalid_json_specification):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=general_rules,
                                    configuration=invalid_json_specification)

    def test_invalid_type(self, str_type_rule, invalid_type_sample):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=str_type_rule,
                                    configuration=invalid_type_sample)

    def test_invalid_dict_type(self, dict_type_rule, invalid_type_sample):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=dict_type_rule,
                                    configuration=invalid_type_sample)

    def test_fixed_index_rule(self, fixed_index_rule, collection_sample):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=fixed_index_rule,
                                    configuration=collection_sample)

    def test_fixed_key_rule(self, fixed_key_rule, dictionary_sample):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=fixed_key_rule,
                                    configuration=dictionary_sample)

    def test_expected_values_rule(self,
                                  expected_values_rule,
                                  dictionary_sample):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=expected_values_rule,
                                    configuration=dictionary_sample)

    def test_custom_rule(self, custom_rule, dictionary_sample):
        inspector = ConfigurationInpector()

        with raises(ValueError):
            inspector.inspect_rules(rules=custom_rule,
                                    configuration=dictionary_sample)
