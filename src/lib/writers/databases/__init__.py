from getpass import getpass


class DatabaseWriter(object):
    @staticmethod
    def rules():
        return {
            'required': {
                'options.engine': {'none': False, 'type': str},
                'options.host': {'none': False, 'type': str},
                'options.database': {'none': False, 'type': str},
                'options.username': {'none': False, 'type': str},
            },
            'optional': {
                'options.schema': {'none': False, 'type': str},
                'options.method': {'none': False, 'type': str},
                'options.port': {'none': False, 'type': int},
            }
        }

    def before_write(self):
        host = self.specification \
                   .get('options') \
                   .get('host')
        user = self.specification \
                   .get('options') \
                   .get('username')
        print(f"Database host: {host}")
        print(f"Username: {user}")
        self.specification['options']['password'] = \
            getpass(f"Type {user} password: ")
