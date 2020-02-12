import random
import unittest

from generator import Generator

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestBooleanGenerator(unittest.TestCase):

    def assert_num_of_records(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.\
            generate_boolean()

        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def assert_all_records_boolean(self):
        gen = Generator(TEST_NUM_OF_RECORDS)
        records = gen.\
            generate_boolean()
        for record in records:
            self.assertIsInstance(record, bool)
