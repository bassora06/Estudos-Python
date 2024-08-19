class Connection():
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def set_port(self, port):
        self.port = port

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    # @staticmethod
    # def soma(x, y):
    #     return x + y


# c1 = Connection()
# print(connection.soma(2, 3))
c1 = Connection.create_with_auth('luiz', 1234)
c1.set_user('postgress')
c1.set_password('fatec')
c1.set_port(1234)
print(c1.user, c1.host, c1.password, c1.port)


    