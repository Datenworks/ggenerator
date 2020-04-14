class SQLWriter(object):
    key = 'sql'

    def __init__(self, formatter, specification):
        self.formatter = formatter
        self.specification = specification

    @staticmethod
    def rules():
        return {
            'required': {
                    'options.engine': {'none': False, 'type': str},
                    'options.host': {'none': False, 'type': str},
                    'options.database': {'none': False, 'type': str},
                    'options.username': {'none': False, 'type': str}
            },
            'optional': {
                'options.method': {'none': False, 'type': str},
                'options.port': {'none': False, 'type': int},
                'options.schema': {'none': False, 'type': str}
            }
        }
