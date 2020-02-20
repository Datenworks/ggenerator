from src.generators.datatypes.boolean import BooleanType
from src.generators.datatypes.char import CharacterType
from src.generators.datatypes.float import FloatType
from src.generators.datatypes.integer import IntegerType
from src.generators.datatypes.sequence_timestamp import TimestampSequenceType
from src.generators.datatypes.sequence import SequenceType
from src.generators.datatypes.string import StringType
from src.generators.datatypes.timestamp import TimestampType


primitive_generators = {BooleanType.key: BooleanType,
                        CharacterType.key: CharacterType}

basic_generators = {FloatType.key: FloatType,
                    IntegerType.key: IntegerType,
                    TimestampSequenceType.key: TimestampSequenceType,
                    SequenceType.key: SequenceType,
                    StringType.key: StringType,
                    TimestampType.key: TimestampType}

generators_map = {}
generators_map.update(primitive_generators)
generators_map.update(basic_generators)
