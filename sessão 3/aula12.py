class Conexao():
    
    #Método construtor
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    #Método de instancia setter
    def setUser(self, user):
        self.user = user

    #Método de instancia setter 
    def setPassword(self, password):
        self.password = password

    @classmethod #Método de classe, Acessa a classe
    def createWithAuth(cls, user, password):
        conexao = cls()
        conexao.user = user
        conexao.password = password
        return conexao
    
    @staticmethod #Função dentro da classe na qual não possui acesso ao self, e nem a cls
    def soma(x, y):
        return x + y

# c1.setUser('MariaDb')
# c1.setPassword('1234')
c1 = Conexao.createWithAuth('luccas', '1234') #Instancia, classe, nome do método da classe 

print(c1.user)
print(c1.password)