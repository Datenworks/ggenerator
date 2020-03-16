from random import uniform


class FloatType:
    key = 'float'
    namespace = 'basic_type'
    optional_arguments = True

    def __init__(self, start_at: float = 0, end_at: float = 100,
                 decimal_floor: int = 3, *args, **kwargs):
        self.start_at = start_at
        self.end_at = end_at
        self.decimal_floor = decimal_floor

    @staticmethod
    def check(generator):
        start_at = generator.get("start_at")
        end_at = generator.get("end_at")
        min_value = -2250738585072014e-308
        max_value = 7976931348623157e+308

        is_start_valid = start_at is not None and \
            start_at > min_value and \
            start_at < max_value
        is_end_valid = end_at is not None and \
            end_at > min_value and \
            end_at < max_value

        return is_start_valid and \
            is_end_valid and \
            start_at < end_at

    def generate(self) -> float:
        return round(uniform(self.start_at, self.end_at), self.decimal_floor)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(0, num_of_records)]
