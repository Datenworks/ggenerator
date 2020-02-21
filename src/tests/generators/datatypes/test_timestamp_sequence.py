import random
from datetime import datetime

from dateutil.parser._parser import ParserError
from src.generators.datatypes.sequence_timestamp import TimestampSequenceType
from src.tests.generators.datatypes.generators_fixtures import generate

TEST_NUM_OF_RECORDS = random.randint(1, 1000)


class TestTimestampGenerator:

    def test_num_of_records(self, generate):
        records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS, start_at="2019-01-01T01:00:00UTC",)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_datetime(self, generate):
        records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS, start_at="2019-01-01T01:00:00UTC",)
        for record in records:
            assert isinstance(record, datetime)

    def test_not_receive_date_format(self, generate):
        import pytest
        with pytest.raises(ParserError):
            records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS, start_at="sfsdfsdfs")

    def test_minutes_sequence_part(self, generate):
        dateparts = ['second', 'minute', 'hour', 'day', 'month', 'year']
        for datepart in dateparts:
            print(datepart)
            records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS, start_at="2019-01-01T01:00:00UTC", datepart=datepart)
            assert len(records) == TEST_NUM_OF_RECORDS