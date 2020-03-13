import inspect
from src.generators.datatypes.boolean import BooleanType
from src.generators.datatypes.char import CharacterType
from src.generators.datatypes.float import FloatType
from src.generators.datatypes.integer import IntegerType
from src.generators.datatypes.sequence_timestamp import TimestampSequenceType
from src.generators.datatypes.sequence import SequenceType
from src.generators.datatypes.string import StringType
from src.generators.datatypes.timestamp import TimestampType
from src.generators.datatypes.fakerproxy import FakerProxy
from pandas import DataFrame, Series


class Metadata(object):
    def __init__(self, locale):
        self.locale = locale
        self.generators = (BooleanType, CharacterType,
                           FloatType, IntegerType,
                           TimestampType, TimestampSequenceType,
                           StringType, SequenceType)
        self.faker = FakerProxy(locale=self.locale)

    def info(self) -> DataFrame:
        return self.__dataframe_info()

    def sample(self, datatype):
        generators_map = self.get_generators_map()
        return generators_map[datatype]['type'].sample() \
            if datatype in generators_map \
            else "Type not found\n"\
                 "Check the specification to use a valid one\n"\
                 "List all the types using the command list-generators"

    def __dataframe_info(self):
        df = DataFrame(columns=['type', 'namespace', 'parameters'])
        for key, value in self.get_generators_map().items():
            info = Series(
                {
                    'namespace': value['namespace'],
                    'type': key,
                    'parameters': value['generator']['arguments']
                })
            df = df.append(info, ignore_index=True)
        return df

    def get_generators_map(self) -> dict:
        generators_map = {
            generator.key: {
                'type': generator,
                'namespace': generator.namespace,
                'generator': {
                    'optional': generator.optional_arguments,
                    'arguments': self.__get_args_info(generator)
                }
            }
            for generator in self.generators}

        faker_types = {
            dtype.__name__: {
                'type': self.faker.__getattribute__(dtype.__name__),
                'namespace': self.faker.__getattribute__(dtype.__name__)
                                       .namespace,
                'generator': {
                    'optional': self.faker.__getattribute__(dtype.__name__)
                                          .optional_arguments,
                    'arguments': self.__get_args_info(
                        self.faker.__getattribute__(dtype.__name__)
                                  .generator_type
                    )
                }
            }
            for dtype in self.faker.list_of_generators
        }

        generators_map.update(faker_types)
        return generators_map

    def __get_args_info(self, func):
        argspec = self.__get_full_arg_spec(func)
        args = argspec.args or []
        if 'self' in args:
            args.remove('self')

        infos = [arg for arg in args]
        return ' | '.join(infos)

    def __get_full_arg_spec(self, func):
        return inspect.getfullargspec(func)
