import unittest
from generator import Generator
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)
TEST_RANDOM_STEP = random.randint(1, 1000)


class TestSequenceGenerator(unittest.TestCase):

    def assert_num_of_records(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_sequence(0, TEST_RANDOM_STEP)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def assert_all_records_integer(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_sequence(0, TEST_RANDOM_STEP)
        for record in records:
            self.assertIsInstance(record, int)

    def assert_step_sequence(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.generate_sequence(0, TEST_RANDOM_STEP)
        end_sublist = records[1:]
        start_sublist = records[:-1]
        differences_list = \
            [second - first
             for (first, second) in zip(start_sublist, end_sublist)]
        for difference in differences_list:
            self.assertEqual(difference, TEST_RANDOM_STEP)
