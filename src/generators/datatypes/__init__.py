from src.generators.datatypes.boolean import BooleanType
from src.generators.datatypes.char import CharacterType
from src.generators.datatypes.float import FloatType
from src.generators.datatypes.integer import IntegerType
from src.generators.datatypes.sequence_timestamp import TimestampSequenceType
from src.generators.datatypes.sequence import SequenceType
from src.generators.datatypes.string import StringType
from src.generators.datatypes.timestamp import TimestampType
from src.generators.datatypes.fakerproxy import FakerProxy


def get_generators_map(locale: str = None):
    primitive_generators = {
        BooleanType.key: {
            'type': BooleanType,
            'generator': {
                'optional': True,
                'arguments': []
            }
        },
        CharacterType.key: {
            'type': CharacterType,
            'generator': {
                'optional': True,
                'arguments': []
            }
        }}

    basic_generators = {
        FloatType.key: {
            'type': FloatType,
            'generator': {
                'optional': True,
                'arguments': ['start_at', 'end_at']
            }
        },
        IntegerType.key: {
            'type': IntegerType,
            'generator': {
                'optional': True,
                'arguments': ['start_at', 'end_at']
            }
        },
        TimestampSequenceType.key: {
            'type': TimestampSequenceType,
            'generator': {
                'optional': False,
                'arguments': ['start_at']
            }
        },
        SequenceType.key: {
            'type': SequenceType,
            'generator': {
                'optional': True,
                'arguments': ['start_at']
            }
        },
        StringType.key: {
            'type': StringType,
            'generator': {
                'optional': True,
                'arguments': ['length']
            }
        },
        TimestampType.key: {
            'type': TimestampType,
            'generator': {
                'optional': False,
                'arguments': ['start_at', 'end_at']
            }
        }}

    faker_proxy = FakerProxy(locale=locale)
    faker_types = {
        dtype.__name__: {
            'type': faker_proxy.__getattribute__(dtype.__name__),
            'generator': {
                'optional': True,
                'arguments': []
            }
        }
        for dtype in faker_proxy.datatypes
    }

    generators_map = {}
    generators_map.update(primitive_generators)
    generators_map.update(basic_generators)
    generators_map.update(faker_types)
    return generators_map
