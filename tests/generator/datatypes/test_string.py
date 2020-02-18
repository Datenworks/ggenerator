from generator.datatypes.string import StringType
from tests.generator.datatypes.generators_fixtures import generate
import random

TEST_NUM_OF_RECORDS = random.randint(1, 10000)
TEST_LENGTH_OF_STRING = random.randint(1, 10000)


class TestStringGenerator:

    def test_num_of_records(self, generate):
        records = generate(StringType, TEST_NUM_OF_RECORDS, length=TEST_LENGTH_OF_STRING)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_string(self, generate):
        records = generate(StringType, TEST_NUM_OF_RECORDS, length=TEST_LENGTH_OF_STRING)
        for record in records:
            assert isinstance(record, str)

    def test_length_strings(self, generate):
        records = generate(StringType, TEST_NUM_OF_RECORDS, length=TEST_LENGTH_OF_STRING)
        for record in records:
            assert len(record) == TEST_LENGTH_OF_STRING
