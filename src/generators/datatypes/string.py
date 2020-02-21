from src.generators.datatypes.char import CharacterType


class StringType:
    key = 'string'

    def __init__(self, length: int = 40):
        self.length = length
        self.character = CharacterType

    @staticmethod
    def check(generator):
        length = generator.get("length")
        return length > 0

    def generate(self) -> str:
        return "".join(self.character().generate_records(self.length))

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(num_of_records)]
