from src.generators.datatypes.faker_custom.pt_BR.cep import CepProvider


class TestCep:
    def test_cep_with_mask(self):
        cepProvider = CepProvider('address')
        cep = cepProvider.postcode(True)
        assert isinstance(cep, str)
        assert cep[5] == '-'
        assert len(cep) == 9

    def test_cep_without_mask(self):
        cepProvider = CepProvider('address')
        cep = cepProvider.postcode(False)
        assert isinstance(cep, str)
        assert cep[5] != '-'
        assert len(cep) == 8
