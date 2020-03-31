import random

from src.generators.datatypes.sequence import SequenceType
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501

TEST_NUM_OF_RECORDS = random.randint(1, 10000)
TEST_RANDOM_STEP = random.randint(1, 1000)


class TestSequenceGenerator:

    def test_num_of_records(self, generate):
        records = generate(SequenceType,
                           TEST_NUM_OF_RECORDS,
                           step=TEST_RANDOM_STEP)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_integer(self, generate):
        records = generate(SequenceType,
                           TEST_NUM_OF_RECORDS,
                           step=TEST_RANDOM_STEP)
        for record in records:
            assert isinstance(record, int)

    def test_step_sequence(self, generate):
        records = generate(SequenceType,
                           TEST_NUM_OF_RECORDS,
                           step=TEST_RANDOM_STEP)
        end_sublist = records[1:]
        start_sublist = records[:-1]
        differences_list = \
            [second - first
             for (first, second) in zip(start_sublist, end_sublist)]
        for difference in differences_list:
            assert difference == TEST_RANDOM_STEP
