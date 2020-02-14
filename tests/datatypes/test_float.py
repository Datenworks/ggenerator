import random
import unittest

from generator.datatypes.float import FloatType

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestFloatGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = FloatType(start_at=0, end_at=100)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_float(self):
        gen = FloatType(start_at=0, end_at=100)
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, float)
