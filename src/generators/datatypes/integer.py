from random import randint


class IntegerType:
    key = 'integer'
    namespace = 'basic_type'
    optional_arguments = True

    def __init__(self, start_at: int = 0, end_at: int = 100,
                 *args, **kwargs):
        self.start_at = start_at
        self.end_at = end_at

    @staticmethod
    def rules():
        def validate(value):
            min_ = -2147483648
            max_ = 2147483648
            if value < min_ or value > max_:
                raise ValueError("Integer generator must be "
                                 f"greater than or equals {min_} and "
                                 f"less than or equals {max_}")

        def validate_range(value):
            start_at = value['start_at']
            end_at = value['end_at']
            if start_at > end_at:
                raise ValueError(f"Integer 'start_at' field `{start_at}` "
                                 f"is higher than 'end_at' field `{end_at}`")
        return {'required': {'generator.start_at': {
                                'none': False,
                                'type': int,
                                'custom': [validate]},
                             'generator.end_at': {
                                'none': False,
                                'type': int,
                                'custom': [validate]},
                             'generator': {
                                 'none': False,
                                 'type': dict,
                                 'custom': [validate_range]
                             }},
                'optional': {}}

    @staticmethod
    def sample():
        start_at = 0
        end_at = 100
        return randint(start_at, end_at)

    def generate(self) -> int:
        return randint(self.start_at, self.end_at)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for x in range(0, num_of_records)]
