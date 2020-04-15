from faker.providers.address.pt_BR import Provider as AddressProvider


class CepProvider(AddressProvider):
    namespace = 'address'  # NAMESPACE SHOULD BE ADDRESS

    def postcode(self, mask: bool = True):
        if mask:
            return self.bothify('#####-###')
        else:
            return self.bothify('########')
