from src.generators.datatypes import Metadata
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501


class TestCompanyGenerator:

    def test_cnpj_without_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh_generator = \
            metadata.get_generators_map()['cnpj']['type']

        result = cnh_generator(mask=False).generate()
        assert len(result) == 14
        for elem in result:
            assert str.isnumeric(elem)

    def test_cnpj_with_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh_generator = \
            metadata.get_generators_map()['cnpj']['type']

        result = cnh_generator(mask=True).generate()
        assert len(result) == 18
        assert result[2] == "."
        assert result[6] == "."
        assert result[10] == "/"
        assert result[15] == "-"
        for index in range(len(result)):
            if index != 2 and index != 6 and index != 10 and index != 15:
                assert str.isnumeric(result[index])
