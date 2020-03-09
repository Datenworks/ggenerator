import random


class BooleanType:
    key = 'bool'

    def __init__(self, value=None, *args, **kwargs):
        self.value = value

    @staticmethod
    def check(generator):
        value = generator.get("value")

        if value is not None:
            return value is True or value is False

        return True

    def __generate_random(self):
        return bool(random.getrandbits(1))

    def generate(self) -> bool:
        if self.value is None:
            return self.__generate_random()
        else:
            return self.value

    def generate_records(self, num_of_records) -> list:
        return [self.generate() for _ in range(num_of_records)]
