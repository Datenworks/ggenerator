import unittest
from generator.datatypes.integer import IntegerType
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestIntegerGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = IntegerType(1, 1000)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_integer(self):
        gen = IntegerType(1, 1000)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, int)
