class AzureBlobWriter(object):
    key = 'azure-bs'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def rules():
        return {
            'required': {
                    'options.container': {'none': False, 'type': str},
                    'options.blob': {'none': False, 'type': str}
            },
            'optional': {}
        }
