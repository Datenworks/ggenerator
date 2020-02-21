from pytest import fixture

@fixture
def generate_files():
    yield "dset_name", "dset_format", "dset_path"