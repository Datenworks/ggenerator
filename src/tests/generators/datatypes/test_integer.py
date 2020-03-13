import random

from src.generators.datatypes.integer import IntegerType
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestIntegerGenerator:

    def test_num_of_records(self, generate):
        records = generate(IntegerType,
                           TEST_NUM_OF_RECORDS,
                           start_at=1,
                           end_at=1000)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_sample_records_int(self, generate, sample):
        records = generate(IntegerType,
                           TEST_NUM_OF_RECORDS,
                           start_at=1,
                           end_at=1000)
        sample_record = sample(IntegerType)
        for record in records:
            assert type(record) == type(sample_record)

    def test_all_records_integer(self, generate):
        records = generate(IntegerType,
                           TEST_NUM_OF_RECORDS,
                           start_at=1,
                           end_at=1000)
        for record in records:
            assert isinstance(record, int)
