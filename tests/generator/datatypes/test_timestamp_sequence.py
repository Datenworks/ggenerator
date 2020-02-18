import random
from datetime import datetime

from dateutil.parser._parser import ParserError
from generator.datatypes.sequence_timestamp import TimestampSequenceType
from tests.generator.datatypes.generators_fixtures import generate

TEST_NUM_OF_RECORDS = random.randint(1, 1000)


class TestTimestampGenerator:

    def test_num_of_records(self, generate):
        records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_datetime(self, generate):
        records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS)
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
            records = generate(TimestampSequenceType, TEST_NUM_OF_RECORDS, datepart=datepart)
            assert len(records) == TEST_NUM_OF_RECORDS