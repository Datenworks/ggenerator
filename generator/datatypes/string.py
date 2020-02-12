from generator.datatypes.char import CharacterType


class StringType:
    def __init__(self, length):
        self.length = length
        self.character = CharacterType

    def generate(self, num_of_records) -> list:
        return ["".join(self.character().generate(self.length))
                for _ in range(num_of_records)]
