import random


class BooleanType:
    key = 'bool'
    namespace = 'PrimitiveType'

    def __init__(self, value=None, *args, **kwargs):
        self.value = value

    @staticmethod
    def rules():
        return {'required': {'generator': {'none': False, 'type': bool}},
                'optional': {}}

    @staticmethod
    def sample():
        return bool(random.getrandbits(1))

    def __generate_random(self):
        return bool(random.getrandbits(1))

    def generate(self) -> bool:
        if self.value is None:
            return self.__generate_random()
        else:
            return self.value

    def generate_records(self, num_of_records) -> list:
        return [self.generate() for _ in range(num_of_records)]
