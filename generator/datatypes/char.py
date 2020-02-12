from random import randint


class CharacterType:
    def __init__(self):
        self.ascii_start = 32
        self.ascii_end = 126

    def generate(self, num_of_records) -> list:
        return [chr(randint(self.ascii_start, self.ascii_end))
                for _ in range(num_of_records)]
