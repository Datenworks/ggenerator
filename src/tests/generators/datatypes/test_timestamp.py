import random

from datetime import datetime
from pytest import raises

from src.generators.datatypes.timestamp import TimestampType
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestTimestampGenerator:

    def test_num_of_records(self, generate):
        records = generate(TimestampType, TEST_NUM_OF_RECORDS,
                           start_at="2019-01-01T01:00:00Z",
                           end_at="2019-12-31T23:59:59Z",
                           tz='UTC')
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_datetime(self, generate):
        records = generate(TimestampType, TEST_NUM_OF_RECORDS,
                           start_at="2019-01-01T01:00:00Z",
                           end_at="2019-12-31T23:59:59Z",
                           tz='UTC')
        for record in records:
            assert isinstance(record, datetime)

    def test_sample_records_datetime(self, generate, sample):
        records = generate(TimestampType, TEST_NUM_OF_RECORDS,
                           start_at="2019-01-01T01:00:00Z",
                           end_at="2019-12-31T23:59:59Z",
                           tz='UTC')
        sample_record = sample(TimestampType)
        for record in records:
            assert type(record) == type(sample_record)

    def test_not_receive_date_format(self, generate):
        with raises(ValueError):
            generate(TimestampType, TEST_NUM_OF_RECORDS,
                     start_at="sdsfsdfs",
                     end_at="sfsdfsdfsf",
                     tz='UTC')
