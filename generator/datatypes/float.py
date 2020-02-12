from random import uniform


class FloatType:
    def __init__(self, start_at, end_at):
        self.start_at = start_at
        self.end_at = end_at

    def generate(self, num_of_records) -> list:
        return [uniform(self.start_at, self.end_at)
                for _ in range(0, num_of_records)]
