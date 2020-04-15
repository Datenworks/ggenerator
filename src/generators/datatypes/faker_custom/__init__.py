

from src.generators.datatypes.\
    faker_custom.pt_BR.cep import CepProvider
from src.generators.datatypes.\
    faker_custom.pt_BR.documents import DocumentProvider


class CustomProviders(object):
    providers_list = [CepProvider, DocumentProvider]

    def providers_return(self, providers):
        providers = self.providers_list

        return providers
