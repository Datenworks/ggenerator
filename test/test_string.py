import unittest
from generator import Generator
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)
TEST_LENGTH_OF_STRING = random.randint(1, 10000)


class TestStringGenerator(unittest.TestCase):

    def assert_num_of_records(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_char()
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def assert_all_records_string(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_char()
        for record in records:
            self.assertIsInstance(record, str)

    def assert_length_strings(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_string(TEST_LENGTH_OF_STRING)
        for record in records:
            self.assertEqual(TEST_LENGTH_OF_STRING, len(record))
