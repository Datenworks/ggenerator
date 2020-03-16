class SequenceType:
    key = 'integer:sequence'
    namespace = 'basic_type'
    optional_arguments = True

    def __init__(self, start_at=0, step=1, *args, **kwargs):
        self.start_at = start_at
        self.step = step

    @staticmethod
    def check(generator):
        start_at = generator.get("start_at")
        if not isinstance(start_at, int):
            return False
        return start_at is not None and \
            start_at > -2147483648 and \
            start_at < 2147483648

    @staticmethod
    def sample():
        start_at = 0
        step = 1
        num_of_rows = 8
        return [x for x in range(start_at,
                                 start_at + num_of_rows * step,
                                 step)]

    def generate_records(self, num_of_rows) -> list:
        return self.__generate_sequence(num_of_rows, self.step)

    def __generate_sequence(self, num_of_rows, step) -> list:
        return [x for x in range(self.start_at,
                                 self.start_at + num_of_rows * step,
                                 step)]
