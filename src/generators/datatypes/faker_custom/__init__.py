from src.generators.datatypes.faker_custom.address.pt_BR import CepProvider
from src.generators.datatypes.faker_custom.ssn.pt_BR import DocumentProvider
from src.generators.datatypes.faker_custom.company.pt_BR import CompanyProvider

custom_providers = {
    'pt_BR': [DocumentProvider, CepProvider, CompanyProvider]
}
