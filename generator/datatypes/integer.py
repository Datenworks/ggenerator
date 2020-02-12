from random import randint


class IntegerType:
    def __init__(self, start_at, end_at):
        self.start_at = start_at
        self.end_at = end_at

    def generate(self, num_of_records) -> list:
        return [randint(self.start_at, self.end_at)
                for x in range(0, num_of_records)]

    def generate_sequence(self, step) -> list:
        return [x for x in range(self.start_at, self.end_at, step)]
