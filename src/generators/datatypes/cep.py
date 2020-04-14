from faker.providers.address import BaseProvider
from faker import Faker


class CepProvider(BaseProvider):
    namespace = 'address'  # NAMESPACE SHOULD BE ADDRESS

    def __init__(self, locale='pt_BR'):
        self.locale = locale

    def cep(self, mask=False):
        self.mask = mask
        self.fake = Faker(locale='pt_BR')
        cep = self.fake.postcode()
        output = ""
        if mask is False:
            if '-' in cep:
                output = f"{cep[0:5]}{cep[6:9]}"
            else:
                output = cep
        if mask is True:
            if '-' not in cep:
                output = cep[0:5] + '-' + cep[5:8]
            else:
                output = cep
        return output
