import random
import string


class CharacterType:
    key = 'char'
    namespace = 'PrimitiveType'

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def check(generator):
        return True

    @staticmethod
    def sample():
        return random.choice(string.ascii_letters)

    def generate(self) -> str:
        return random.choice(string.ascii_letters)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(num_of_records)]
