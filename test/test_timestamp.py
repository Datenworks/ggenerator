import random
import unittest
from datetime import datetime

from dateutil.parser import parse
from dateutil.parser._parser import ParserError
from generator import Generator

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestTimestampGenerator(unittest.TestCase):

    def assert_num_of_records(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.\
            generate_timestamp("2019-01-01T01:00:00UTC",
                               "2019-12-31T23:59:59UTC")
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def assert_all_records_datetime(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.\
            generate_timestamp("2019-01-01T01:00:00UTC",
                               "2019-12-31T23:59:59UTC")
        for record in records:
            self.assertIsInstance(parse(record), datetime)

    def assert_not_receive_date_format(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        with self.assertRaises(ParserError):
            gen.generate_timestamp("sdasdasdas",
                                   "asdasdasd")
