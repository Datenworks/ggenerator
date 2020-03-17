from pytest import raises

from src.lib.config.fields import FieldsConfiguration
from src.lib.config.inspector import ConfigurationInpector
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestFieldsConfiguration(object):
    """Unit-test of TestFieldsConfiguration class"""

    def test_valid_csv_specification(self, valid_csv_specification):
        inspector = ConfigurationInpector()

        dataset = valid_csv_specification['datasets']['valid']
        fields = dataset['fields']

        for field in fields:
            rules = FieldsConfiguration.get_rules(field, dataset['locale'])
            required = rules['required']
            inspect = inspector. \
                inspect_rules(rules=required,
                              configuration=field)
            assert inspect is None

    def test_invalid_csv_configuration(self, invalid_csv_specification):
        inspector = ConfigurationInpector()
        dataset = invalid_csv_specification['datasets']['invalid']
        fields = dataset['fields']

        for field in fields:
            with raises(ValueError):
                rules = FieldsConfiguration.get_rules(field, dataset['locale'])
                required = rules['required']

                inspector. \
                    inspect_rules(rules=required,
                                  configuration=field)
