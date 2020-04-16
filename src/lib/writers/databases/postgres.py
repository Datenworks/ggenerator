from sqlalchemy import create_engine
from getpass import getpass


class PostgresDataBaseWritter(object):
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

    def before_write(self):
        host = self.specification \
                   .get('options') \
                   .get('host')
        user = self.specification \
                   .get('options') \
                   .get('username')
        print(f"Database host: {host}")
        print(f"Database username: {user}")
        self.specification['options']['password'] = \
            getpass(f"Type {user} password: ")