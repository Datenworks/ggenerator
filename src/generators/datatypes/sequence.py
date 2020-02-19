class SequenceType:
    key = 'integer:sequence'

    def __init__(self, start_at=1, step=1):
        self.start_at = start_at
        self.step = step

    def generate_records(self, num_of_rows) -> list:
        return self.__generate_sequence(num_of_rows, self.step)

    def __generate_sequence(self, num_of_rows, step) -> list:
        return [x for x in range(self.start_at,
                                 self.start_at + num_of_rows * step,
                                 step)]
