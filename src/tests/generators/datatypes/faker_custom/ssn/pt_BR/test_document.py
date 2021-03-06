from src.generators.datatypes import Metadata
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501


class TestDocumentGenerator:

    def test_cnh_without_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh_generator = \
            metadata.get_generators_map()['cnh']['type']

        result = cnh_generator(mask=False).generate()
        assert len(result) == 11
        for elem in result:
            assert str.isnumeric(elem)

    def test_cnh_with_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh_generator = \
            metadata.get_generators_map()['cnh']['type']

        result = cnh_generator(mask=True).generate()
        assert len(result) == 14
        assert result[3] == " " and result[7] == " " and result[11] == " "
        for index in range(len(result)):
            if index != 3 and index != 7 and index != 11:
                assert str.isnumeric(result[index])

    def test_titulo_eleitor_without_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh_generator = \
            metadata.get_generators_map()['titulo_eleitoral']['type']

        result = cnh_generator(mask=False).generate()
        assert len(result) == 12
        for elem in result:
            assert str.isnumeric(elem)

    def test_titulo_eleitor_with_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh_generator = \
            metadata.get_generators_map()['titulo_eleitoral']['type']

        result = cnh_generator(mask=True).generate()
        assert len(result) == 14
        assert result[4] == " " and result[9] == " "
        for index in range(len(result)):
            if index != 4 and index != 9:
                assert str.isnumeric(result[index])
