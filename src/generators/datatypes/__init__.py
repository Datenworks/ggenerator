import inspect
from src.generators.datatypes.sequence_timestamp import TimestampSequenceType
from src.generators.datatypes.sequence import SequenceType
from src.generators.datatypes.fakerproxy import FakerProxy
from pandas import DataFrame, Series


class Metadata(object):
    def __init__(self, locale):
        self.locale = locale
        self.generators = (TimestampSequenceType, SequenceType)
        self.faker = FakerProxy(locale=self.locale)

    def info(self) -> DataFrame:
        return self.__dataframe_info()

    def sample(self, datatype, *args, **kwargs):
        try:
            return self.__sample(datatype, *args, **kwargs)
        except Exception as err:
            raise Exception(err)

    def __sample(self, datatype, *args, **kwargs):
        generators_map = self.get_generators_map()
        try:
            sample = generators_map[datatype]['type'](**kwargs).generate()
            return sample
        except KeyError:
            raise TypeError("Type not found\n"
                            "Check the specification to use a valid one\n"
                            "List all the types using "
                            "the command list-generators")
        except TypeError:
            raise TypeError(
                "Invalid parameter, "
                "please check the spec to correct name and value type")

        except Exception:
            raise ValueError(
                "Invalid parameter, "
                "please check the spec to correct name and value type")

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
        params = self.__get_parameters(func)
        infos = []
        for arg_name, arg_info in params.items():
            info = f"{arg_name}"
            info += f" | default: {arg_info.default}" \
                if arg_info.default is not inspect._empty\
                else ''

            info += f" | type: {arg_info.annotation.__name__ }"\
                if arg_info.annotation is not inspect._empty\
                else ''

            infos.append(info)

        return '\n'.join(infos)

    def __get_parameters(self, func):
        return inspect.signature(func).parameters
