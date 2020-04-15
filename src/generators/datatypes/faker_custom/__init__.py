from src.generators.datatypes.faker_custom.address.pt_BR import CepProvider
from src.generators.datatypes.faker_custom.ssn.pt_BR import DocumentProvider

custom_providers = {
    'pt_BR': [DocumentProvider, CepProvider]
}
