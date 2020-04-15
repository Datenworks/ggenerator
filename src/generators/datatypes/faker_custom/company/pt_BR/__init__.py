from faker.providers.company.pt_BR import Provider


class CompanyProvider(Provider):
    def cnpj(self, mask: bool = True):
        digits = self.company_id()
        if mask:
            return '{}.{}.{}/{}-{}'.format(digits[:2], digits[2:5],
                                           digits[5:8], digits[8:12],
                                           digits[12:])
        else:
            return self.company_id()
