import random

from src.generators.datatypes.float import FloatType
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501

TEST_NUM_OF_RECORDS = random.randint(1, 10000)


class TestFloatGenerator:

    def test_num_of_records(self, generate):
        records = generate(FloatType,
                           TEST_NUM_OF_RECORDS,
                           start_at=0,
                           end_at=10,
                           decimal_floor=3)
        assert len(records) == TEST_NUM_OF_RECORDS

    def test_all_records_float(self, generate):
        records = generate(FloatType,
                           TEST_NUM_OF_RECORDS,
                           start_at=0,
                           end_at=10,
                           decimal_floor=3)
        for record in records:
            assert isinstance(record, float)
