import unittest
from generator.datatypes.string import StringType
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)
TEST_LENGTH_OF_STRING = random.randint(1, 10000)


class TestStringGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = StringType(TEST_LENGTH_OF_STRING)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_string(self):
        gen = StringType(TEST_LENGTH_OF_STRING)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, str)

    def test_length_strings(self):
        gen = StringType(TEST_LENGTH_OF_STRING)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertEqual(TEST_LENGTH_OF_STRING, len(record))
