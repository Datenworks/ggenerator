from tests.generator.datatypes.generators_fixtures import generate
from generator.datatypes.char import CharacterType

import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestCharGenerator:

    def test_num_of_records(self, generate):
        records = generate(CharacterType, TEST_NUM_OF_RECORDS)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_chr(self, generate):
        records = generate(CharacterType, TEST_NUM_OF_RECORDS)
        for record in records:
            assert isinstance(record, str)

    def test_length_chars(self, generate):
        records = generate(CharacterType, TEST_NUM_OF_RECORDS)
        for record in records:
            assert len(record) == 1
