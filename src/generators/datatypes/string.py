from src.generators.datatypes.char import CharacterType


class StringType:
    key = 'string'
    namespace = 'basic_type'
    optional_arguments = True

    def __init__(self, length: int = 40, *args, **kwargs):
        self.length = length
        self.character = CharacterType

    @staticmethod
    def rules():
        def validate(value):
            if value <= 0:
                raise ValueError("String `length` cannot be less than 0")

        return {'required': {'generator.length': {
                                'none': False,
                                'type': int,
                                'custom': [validate]}},
                'optional': {}}

    @staticmethod
    def sample():
        return "".join(CharacterType().generate_records(40))

    def generate(self) -> str:
        return "".join(self.character().generate_records(self.length))

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(num_of_records)]
