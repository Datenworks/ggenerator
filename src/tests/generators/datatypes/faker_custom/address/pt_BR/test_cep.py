from src.generators.datatypes import Metadata
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501


class TestCep:
    def test_cep_with_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cep_generator = metadata.get_generators_map()['postcode']['type']
        cep = cep_generator(mask=True).generate()
        assert isinstance(cep, str)
        assert cep[5] == '-'
        assert len(cep) == 9

    def test_cep_without_mask(self):
        metadata = Metadata(locale='pt_BR')
        cep_generator = metadata.get_generators_map()['postcode']['type']
        cep = cep_generator(mask=False).generate()
        assert isinstance(cep, str)
        assert cep[5] != '-'
        assert len(cep) == 8
