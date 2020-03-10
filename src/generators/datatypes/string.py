from src.generators.datatypes.char import CharacterType


class StringType:
    key = 'string'
    namespace = 'BasicType'

    def __init__(self, length: int = 40):
        self.length = length
        self.character = CharacterType

    @staticmethod
    def check(generator):
        length = generator.get("length")
        return length > 0

    @staticmethod
    def sample():
        return "".join(CharacterType().generate_records(40))

    def generate(self) -> str:
        return "".join(self.character().generate_records(self.length))

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(num_of_records)]
