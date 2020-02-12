from generator.datatypes.integer import IntegerType


class SequenceType:
    def __init__(self, start_at):
        self.integer = IntegerType
        self.start_at = start_at

    def generate(self, num_of_rows, step=1) -> list:
        return self.integer(self.start_at,
                            self.start_at + num_of_rows * step) \
                                .generate_sequence(step=step)
