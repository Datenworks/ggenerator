from faker import Faker
import inspect


class FakerProxy(object):
    def __init__(self, locale: str):
        self.faker = Faker(locale=locale)
        self.datatypes = self.__get_datatypes()
        self.__infer_types()

    def __get_datatypes(self):
        return [generator for _, generator
                in self.faker.factories[0].__dict__.items()
                if callable(generator)]

    def __infer_types(self):
        for dtype in self.datatypes:
            namespace = self.__get_namespace(dtype)
            self.__setattr__(dtype.__name__, FakerType(dtype, namespace))

    def __get_namespace(self, obj):
        try:
            return inspect.getmodule(obj).__name__.split('.')[2]
        except IndexError:
            return "generic"


class FakerType(object):
    def __init__(self, dtype, namespace):
        self.dtype = dtype
        self.key = dtype.__name__
        self.namespace = namespace

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

    def generate(self):
        return self.__parse_data(self.dtype(*self.args, **self.kwargs))

    def generate_records(self, num_of_records):
        return [self.generate(*self.args, **self.kwargs)
                for _ in range(num_of_records)]

    def __parse_data(self, data):
        if isinstance(data, str):
            return data.replace('\n', ' ')
        return data

    @staticmethod
    def check(generator):
        return True
