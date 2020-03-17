from faker import Faker
import inspect


class FakerProxy(object):
    def __init__(self, locale: str):
        self.faker = Faker(locale=locale)
        self.blacklist_namespaces = ['generic']
        self.blacklist_generator = ['time_series']
        self.list_of_generators = self.__generators_types()
        self.__infer_types()

    def __generators_types(self) -> list:
        def is_not_namespace_blacklist(generator):
            namespace = self.__get_namespace(generator)
            return namespace not in self.blacklist_namespaces

        def is_not_generator_blacklist(generator):
            return generator.__name__ not in self.blacklist_generator

        return [generator for _, generator
                in self.faker.factories[0].__dict__.items()
                if callable(generator) and
                is_not_generator_blacklist(generator) and
                is_not_namespace_blacklist(generator)]

    def __infer_types(self) -> None:
        for generator_type in self.list_of_generators:
            namespace = self.__get_namespace(generator_type)
            self.__infer_type(generator_type=generator_type,
                              namespace=namespace)

    def __infer_type(self, generator_type, namespace) -> None:
        self.__setattr__(generator_type.__name__,
                         FakerType(generator_type=generator_type,
                                   namespace=namespace))

    def __get_type_info(self, generator_type):
        return inspect.getfullargspec(generator_type)

    def __get_namespace(self, obj) -> str:
        try:
            return inspect.getmodule(obj).__name__.split('.')[2]
        except IndexError:
            return "generic"


class FakerType(object):
    optional_arguments = True

    def __init__(self, generator_type, namespace):
        self.generator_type = generator_type
        self.key = generator_type.__name__
        self.namespace = namespace

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

    def generate(self):
        return self.__parse_data(self.generator_type(*self.args,
                                                     **self.kwargs))

    def generate_records(self, num_of_records):
        return [self.generate()
                for _ in range(num_of_records)]

    def __parse_data(self, data):
        if isinstance(data, str):
            data = self.__remove_break_lines(data)
        return data

    def __remove_break_lines(self, data: str):
        return data.replace('\n', ' ')

    @staticmethod
    def rules():
        return {'required': {},
                'optional': {}}

    def sample(self):
        return self.__parse_data(self.generator_type())
