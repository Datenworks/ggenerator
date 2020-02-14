import random
import unittest

from generator.datatypes.boolean import BooleanType

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestBooleanGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = BooleanType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)

        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_boolean(self):
        gen = BooleanType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, bool)
