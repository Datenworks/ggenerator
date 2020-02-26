from random import uniform


class FloatType:
    key = 'float'

    def __init__(self, start_at: float = 0, end_at: float = 100,
                 decimal_floor: int = 3):
        self.start_at = start_at
        self.end_at = end_at
        self.decimal_floor = decimal_floor

    @staticmethod
    def check(generator):
        start_at = generator.get("start_at")
        end_at = generator.get("end_at")
        return start_at > -2250738585072014e-308 and \
            start_at < 7976931348623157e+308 and \
            end_at > -2250738585072014e-308 and \
            end_at < 7976931348623157e+308

    def generate(self) -> float:
        return round(uniform(self.start_at, self.end_at), self.decimal_floor)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(0, num_of_records)]
