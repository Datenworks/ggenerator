from pytest import raises

from src.lib.config.serializers import SerializersConfiguration
from src.tests.lib.config.fixtures import *  # noqa: F403, F401


class TestSerializersConfiguration(object):
    """Unit-test of TestSerializersConfiguration class"""

    def test_file(self, file_writer_sample):
        rules = SerializersConfiguration.get_rules(file_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_mysql(self, mysql_writer_sample):
        rules = SerializersConfiguration.get_rules(mysql_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_postgresql(self, postgresql_writer_sample):
        rules = SerializersConfiguration.get_rules(postgresql_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_s3(self, s3_writer_sample):
        rules = SerializersConfiguration.get_rules(s3_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_s3_url(self, s3_url_writer_sample):
        rules = SerializersConfiguration.get_rules(s3_url_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_gcs(self, gcs_writer_sample):
        rules = SerializersConfiguration.get_rules(gcs_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_gcs_url(self, gcs_url_writer_sample):
        rules = SerializersConfiguration.get_rules(gcs_url_writer_sample)

        assert rules is not None
        assert isinstance(rules, dict) is True

    def test_unknown(self, unknown_writer_sample):
        with raises(ValueError):
            SerializersConfiguration.get_rules(unknown_writer_sample)
