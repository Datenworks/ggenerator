from faker.providers.ssn.pt_BR import Provider as SsnProvider


class DocumentProvider(SsnProvider):
    namespace = 'ssn'

    def titulo_eleitoral(self, mask: bool = True):
        if mask:
            return self.bothify('#### #### ####')
        else:
            return self.bothify('############')

    def cnh(self, mask: bool = True):
        if mask:
            return self.bothify('### ### ### ##')
        else:
            return self.bothify('###########')
