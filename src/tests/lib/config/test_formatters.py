from pytest import raises

from src.lib.config.formatters import FormattersConfiguration
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestFormattersConfiguration(object):
    """Unit-test of TestFormattersConfiguration class"""

    def test_csv(self, csv_format_sample):
        rules = FormattersConfiguration.get_rules(csv_format_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_json(self, json_format_sample):
        rules = FormattersConfiguration.get_rules(json_format_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_sql(self, sql_format_sample):
        rules = FormattersConfiguration.get_rules(sql_format_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_unknown(self, unknown_format_sample):
        with raises(ValueError):
            FormattersConfiguration.get_rules(unknown_format_sample)
