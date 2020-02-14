import random
import unittest
from datetime import datetime

from dateutil.parser import parse
from dateutil.parser._parser import ParserError
from generator.datatypes.timestamp import TimestampType

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestTimestampGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = TimestampType(start_at="2019-01-01T01:00:00UTC",
                            end_at="2019-12-31T23:59:59UTC",
                            tz='UTC')
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_datetime(self):
        gen = TimestampType(start_at="2019-01-01T01:00:00UTC",
                            end_at="2019-12-31T23:59:59UTC",
                            tz='UTC')
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, datetime)

    def test_not_receive_date_format(self):
        with self.assertRaises(ParserError):
            gen = TimestampType(start_at="asdasdasd",
                                end_at="asdasdasd",
                                tz='UTC')
            gen.generate_records(TEST_NUM_OF_RECORDS)