from random import uniform


class BooleanType:
    def generate(self, num_of_records) -> list:
        return [round(uniform(0, 1)) == 1 for _ in range(num_of_records)]
