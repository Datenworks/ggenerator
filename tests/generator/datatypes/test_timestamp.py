import random
from datetime import datetime

from dateutil.parser._parser import ParserError
from generator.datatypes.timestamp import TimestampType
from tests.generator.datatypes.generators_fixtures import generate

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestTimestampGenerator:

    def test_num_of_records(self, generate):
        records = generate(TimestampType, TEST_NUM_OF_RECORDS,
                           start_at="2019-01-01T01:00:00UTC",
                           end_at="2019-12-31T23:59:59UTC",
                           tz='UTC')
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_datetime(self, generate):
        records = generate(TimestampType, TEST_NUM_OF_RECORDS,
                           start_at="2019-01-01T01:00:00UTC",
                           end_at="2019-12-31T23:59:59UTC",
                           tz='UTC')
        for record in records:
            assert isinstance(record, datetime)

    def test_not_receive_date_format(self, generate):
        import pytest
        with pytest.raises(ParserError):
            records = generate(TimestampType, TEST_NUM_OF_RECORDS,
                           start_at="sdsfsdfs",
                           end_at="sfsdfsdfsf",
                           tz='UTC')