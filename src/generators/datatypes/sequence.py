from typing import List


class SequenceType:
    key = 'integer:sequence'
    namespace = 'basic_type'
    optional_arguments = True

    def __init__(self, start_at=0, step=1, *args, **kwargs):
        self.start_at = start_at
        self.step = step

    @staticmethod
    def rules():
        def validate(value):
            min_ = -2147483648
            max_ = 2147483648
            if value < min_ or value > max_:
                raise ValueError("Sequence `start_at` generator must be "
                                 f"greater than or equals {min_} and "
                                 f"less than or equals {max_}")
        return {'required': {'generator.start_at': {'none': False,
                                                    'type': int,
                                                    'custom': [validate]}},
                'optional': {}}

    def generate(self, num_of_records: int = 5) -> List[int]:
        return self.generate_records(num_of_records=num_of_records)

    def generate_records(self, num_of_records, progress=None) -> List[int]:
        return self.__generate_sequence(num_of_rows=num_of_records,
                                        step=self.step,
                                        progress=progress)

    def __generate_sequence(self,
                            num_of_rows,
                            step,
                            progress=None) -> List[int]:
        results = []
        for x in range(self.start_at,
                       self.start_at + num_of_rows * step,
                       step):
            results.append(x)
            progress and progress()
        return results
