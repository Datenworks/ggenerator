import random

from src.generators.datatypes.string import StringType
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501

TEST_NUM_OF_RECORDS = random.randint(1, 10000)
TEST_LENGTH_OF_STRING = random.randint(1, 15)


class TestStringGenerator:

    def test_num_of_records(self, generate):
        records = generate(StringType,
                           TEST_NUM_OF_RECORDS,
                           length=TEST_LENGTH_OF_STRING)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_string(self, generate):
        records = generate(StringType,
                           TEST_NUM_OF_RECORDS,
                           length=TEST_LENGTH_OF_STRING)
        for record in records:
            assert isinstance(record, str)

    def test_sample_records_string(self, generate, sample):
        records = generate(StringType,
                           TEST_NUM_OF_RECORDS,
                           length=TEST_LENGTH_OF_STRING)
        sample_record = sample(StringType)
        for record in records:
            assert type(record) == type(sample_record)

    def test_length_strings(self, generate):
        records = generate(StringType,
                           TEST_NUM_OF_RECORDS,
                           length=TEST_LENGTH_OF_STRING)
        for record in records:
            assert len(record) == TEST_LENGTH_OF_STRING
