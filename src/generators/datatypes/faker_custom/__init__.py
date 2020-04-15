from src.generators.datatypes.\
    faker_custom.pt_BR.cep import CepProvider
from src.generators.datatypes.\
    faker_custom.pt_BR.ssn import DocumentProvider


custom_providers = {
    'pt_BR': [DocumentProvider, CepProvider]
}
