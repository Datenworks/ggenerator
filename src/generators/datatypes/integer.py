from random import randint


class IntegerType:
    key = 'integer'

    def __init__(self, start_at: int = 0, end_at: int = 100):
        self.start_at = start_at
        self.end_at = end_at

    @staticmethod
    def check(generator):
        start_at = generator.get("start_at")
        end_at = generator.get("end_at")
        return start_at is not None and \
            start_at > -2147483648 and \
            start_at < 2147483648 and \
            end_at is not None and \
            end_at > -2147483648 and \
            end_at < 2147483648

    def generate(self) -> int:
        return randint(self.start_at, self.end_at)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for x in range(0, num_of_records)]
