import unittest
from generator import Generator
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestCharGenerator(unittest.TestCase):

    def assert_num_of_records(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_char()
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def assert_all_records_chr(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_char()
        for record in records:
            self.assertIsInstance(record, str)

    def assert_length_chars(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_char()
        for record in records:
            self.assertEqual(1, len(record))
