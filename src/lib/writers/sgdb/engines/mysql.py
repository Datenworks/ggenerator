from sqlalchemy import create_engine


class MySQLEngine(object):
    key = 'mysql'

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self, user, password, database):
        return create_engine('mysql+mysqlconnector://'
                             f'{user}:'
                             f'{password}@'
                             f'{self.host}:'
                             f'{self.port}/'
                             f'{database}')

    def cli(self):
        pass
