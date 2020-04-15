from src.generators.datatypes.faker_custom.address.pt_BR import CepProvider


class TestCep:
    def test_cep_with_mask(self):
        cepProvider = CepProvider()
        cep = cepProvider.postcode(mask=True)
        assert isinstance(cep, str)
        assert cep[5] == '-'
        assert len(cep) == 9

    def test_cep_without_mask(self):
        cepProvider = CepProvider()
        cep = cepProvider.postcode(mask=False)
        assert isinstance(cep, str)
        assert cep[5] != '-'
        assert len(cep) == 8
