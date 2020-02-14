import random
import unittest
from datetime import datetime

from dateutil.parser import parse
from dateutil.parser._parser import ParserError
from generator.datatypes.sequence_timestamp import TimestampSequenceType

TEST_NUM_OF_RECORDS = random.randint(1, 1000)


class TestTimestampGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = TimestampSequenceType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_datetime(self):
        gen = TimestampSequenceType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, datetime)

    def test_not_receive_date_format(self):
        with self.assertRaises(ParserError):
            gen = TimestampSequenceType(start_at="asdasdasd")
            gen.generate_records(TEST_NUM_OF_RECORDS)

    def test_minutes_sequence_part(self):
        dateparts = ['second', 'minute', 'hour', 'day', 'month', 'year']
        for datepart in dateparts:
            print(datepart)
            gen = TimestampSequenceType(datepart=datepart)
            records = gen.generate_records(8028)
            self.assertEqual(8028, len(records))