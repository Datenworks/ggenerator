from src.generators.datatypes import Metadata
from src.tests.generators.datatypes.generators_fixtures import *  # noqa: F403, F401, E501


class TestDocumentGenerator:

    def test_cnh_without_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh = metadata.get_generators_map()['cnh']['type']

        result = cnh(mask=False).generate()
        assert len(result) == 11
        for elem in result:
            assert str.isnumeric(elem)

    def test_cnh_with_mask(self, generate):
        metadata = Metadata(locale='pt_BR')
        cnh = metadata.get_generators_map()['cnh']['type']

        result = cnh(mask=True).generate()
        assert len(result) == 14
        assert result[3] == " " and result[7] == " " and result[11]
        for index in range(len(result)):
            if index != 3 and index != 7 and index != 11:
                assert str.isnumeric(result[index])
