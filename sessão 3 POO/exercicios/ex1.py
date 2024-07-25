class Conexao():
    
    @classmethod
    def connection(cls, host, user, password, db_name):
        connection = cls()
        connection.host = host
        connection.user = user
        connection.password = password
        connection.db_name = db_name
        return connection
    

c1 = Conexao.connection('localhost', 'root', '', 'empresa')

if c1.host == 'localhost':
    if c1.user == 'root':
        if c1.password == '':
            if c1.db_name == 'empresa':
                print('Banco de dados conectado com sucesso')
            else:
                print('O banco de dados não foi conectado')
        else:
            print('O banco de dados não foi conectado')
    else:
        print('O banco de dados não foi conectado')
else:
    print('O banco de dados não foi conectado')
