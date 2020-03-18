from pytest import fixture


def generate_records(type_generator, num_of_records):
    return type_generator.generate_records(num_of_records)


@fixture
def generate():
    def _generate(DataType, num_of_records, **kwargs):
        return generate_records(DataType(**kwargs), num_of_records)
    return _generate
