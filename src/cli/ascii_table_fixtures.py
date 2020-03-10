import random
from src.generators.datatypes import *


def typeSamples(type):
    bool1 = BooleanType()
    char1 = CharacterType()
    float1 = FloatType()
    integer1 = IntegerType()
    sequence_timestamp1 = TimestampSequenceType(
        "1994-02-20T15:48:33-03:00")
    sequence1 = SequenceType()
    string1 = StringType()
    timestamp1 = TimestampType(
        "1994-02-20T15:48:33-03:00", "2012-07-31T19:55:00-03:00"
    )
    if type == 'boolean':
        return bool1.generate()
        # return boolean.BooleanType.generate() SUGESTÃO LUKITA

    if type == 'char':
        return char1.generate()

    if type == 'float':
        return float1.generate()

    if type == 'integer':
        return integer1.generate()

    if type == 'timestamp:sequence':
        return sequence_timestamp1.generate_records(1)

    if type == 'integer:sequence':
        return sequence1.generate_records(8)

    if type == 'string':
        return string1.generate()

    if type == 'timestamp':
        return timestamp1.generate()
