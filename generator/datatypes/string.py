from generator.datatypes.char import CharacterType


class StringType:
    def __init__(self, length: int = 40):
        self.length = length
        self.character = CharacterType

    def generate(self) -> str:
        return "".join(self.character().generate_records(self.length))

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(num_of_records)]
