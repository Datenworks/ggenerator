import random


class BooleanType:
    key = 'boolean'

    def generate(self) -> bool:
        return bool(random.getrandbits(1))

    def generate_records(self, num_of_records) -> list:
        return [self.generate() for _ in range(num_of_records)]
