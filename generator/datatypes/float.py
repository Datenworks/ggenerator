from random import uniform


class FloatType:
    def __init__(self, start_at: float = 0, end_at: float = 100,
                 decimal_floor: int = 3):
        self.start_at = start_at
        self.end_at = end_at
        self.decimal_floor = decimal_floor

    def generate(self) -> float:
        return round(uniform(self.start_at, self.end_at), self.decimal_floor)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(0, num_of_records)]
