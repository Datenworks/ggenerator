import unittest
from generator.datatypes.char import CharacterType
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestCharGenerator(unittest.TestCase):

    def test_num_of_records(self):
        gen = CharacterType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        self.assertEqual(TEST_NUM_OF_RECORDS, len(records))

    def test_all_records_chr(self):
        gen = CharacterType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertIsInstance(record, str)

    def test_length_chars(self):
        gen = CharacterType()
        records = gen.generate_records(TEST_NUM_OF_RECORDS)
        for record in records:
            self.assertEqual(1, len(record))
