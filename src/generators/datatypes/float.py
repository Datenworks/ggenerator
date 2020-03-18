from random import uniform


class FloatType:
    key = 'float'
    namespace = 'basic_type'
    optional_arguments = True

    def __init__(self, start_at: float = 0, end_at: float = 100,
                 decimal_floor: int = 3, *args, **kwargs):
        self.start_at = start_at
        self.end_at = end_at
        self.decimal_floor = decimal_floor

    @staticmethod
    def rules():
        def validate(value):
            min_ = -1.7976931348623157e+308
            max_ = 1.7976931348623157e+308
            if value < min_ or value > max_:
                raise ValueError("Float generator must be "
                                 f"greater than or equals {min_} and "
                                 f"less than or equals {max_}")

        def validate_range(value):
            start_at = value['start_at']
            end_at = value['end_at']
            if start_at > end_at:
                raise ValueError(f"Float 'start_at' field `{start_at}` "
                                 f"is higher than 'end_at' field `{end_at}`")
        return {'required': {'generator.start_at': {
                                'none': False,
                                'type': float,
                                'custom': [validate]},
                             'generator.end_at': {
                                'none': False,
                                'type': float,
                                'custom': [validate]},
                             'generator': {
                                 'none': False,
                                 'type': dict,
                                 'custom': [validate_range]
                             }},
                'optional': {}}

    def generate(self) -> float:
        return round(uniform(self.start_at, self.end_at), self.decimal_floor)

    def generate_records(self, num_of_records) -> list:
        return [self.generate()
                for _ in range(0, num_of_records)]
