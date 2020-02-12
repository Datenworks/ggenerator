import unittest
from generator import Generator
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestIntegerGenerator(unittest.TestCase):

    def assert_num_of_records(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_integer(0, 1000)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def assert_all_records_integer(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_integer(0, 1000)
        for record in records:
            self.assertIsInstance(record, int)
