from random import randint


class IntegerType:
    def __init__(self, start_at: int = 0, end_at: int = 100):
        self.start_at = start_at
        self.end_at = end_at

    def generate(self) -> int:
        return randint(self.start_at, self.end_at)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for x in range(0, num_of_records)]
