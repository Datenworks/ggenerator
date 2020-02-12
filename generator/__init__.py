from generator.datatypes.integer import IntegerType
from generator.datatypes.sequence import SequenceType
from generator.datatypes.char import CharacterType
from generator.datatypes.string import StringType
from generator.datatypes.float import FloatType
from generator.datatypes.timestamp import TimestampType
from generator.datatypes.boolean import BooleanType


class Generator:
    def __init__(self, num_of_records):
        self.num_of_records = num_of_records
        self.integer = IntegerType
        self.sequence = SequenceType
        self.character = CharacterType
        self.string = StringType
        self.float = FloatType
        self.timestamp = TimestampType
        self.boolean = BooleanType

    def generate_integer(self, start_at: int, end_at: int):
        return self.integer(start_at, end_at) \
            .generate(self.num_of_records)

    def generate_sequence(self, start_at: int, step):
        return self.sequence(start_at) \
            .generate(self.num_of_records, step)

    def generate_char(self):
        return self.character().generate(self.num_of_records)

    def generate_string(self, length: int):
        return self.string(length=length).generate(self.num_of_records)

    def generate_float(self, start_at: float, end_at: float):
        return self.float(start_at=start_at, end_at=end_at)\
            .generate(num_of_records=self.num_of_records)

    def generate_timestamp(self, start_at: str, end_at: str):
        """
        MUST RECEIVE A ISO-8601 DATE FORMAT
        """
        return self.timestamp(start_at=start_at, end_at=end_at)\
            .generate(num_of_records=self.num_of_records)

    def generate_boolean(self):
        return self.boolean().generate(num_of_records=self.num_of_records)
