from src.generators.datatypes.cep import CepProvider


class TestCep:
    def test_cep_with_mask(self):
        cepProvider = CepProvider()
        cep = cepProvider.cep(True)
        assert isinstance(cep, str)
        assert cep[5] == '-'
        assert len(cep) == 9

    def test_cep_without_mask(self):
        cepProvider = CepProvider()
        cep = cepProvider.cep(False)
        assert isinstance(cep, str)
        assert cep[5] != '-'
        assert len(cep) == 8
