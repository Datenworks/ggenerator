import random

from src.generators.datatypes.boolean import BooleanType
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestBooleanGenerator:

    def test_num_of_records(self, generate):
        records = generate(BooleanType, TEST_NUM_OF_RECORDS)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_boolean(self, generate):
        records = generate(BooleanType, TEST_NUM_OF_RECORDS)
        for record in records:
            assert isinstance(record, bool)
