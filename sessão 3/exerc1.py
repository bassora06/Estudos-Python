from abc import ABC

class Conta(ABC):
    def __init__(self, agencia : int, numeroConta: int, saldo: float):
        self._agencia = agencia
        self._numeroConta = numeroConta
        self._saldo = saldo
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor, limite):
        self.limite = limite
        self._saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, agencia, numeroConta, saldo):
        super().__init__(agencia, numeroConta, saldo)

    def sacar(self, valor, limite = 2000):
        return super().sacar(valor, limite)
    
    def depositar(self, valor):
        return super().depositar(valor)
    

class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numeroConta, saldo):
        super().__init__(agencia, numeroConta, saldo)

    def depositar(self, valor):
        return super().depositar(valor)
    
    def sacar(self, valor, limite = 1000):
        return super().sacar(valor, limite)



class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @nome.setter
    def idade(self, idade):
        self._idade = idade



class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._conta = None


class Banco():
    def __init__(self):
        self._cliente = None
        self._conta= None

    
    def checarCliente(self):
        if self._cliente.nome: 
            print('A pessoa é cliente do banco')
        print('A pessoa não é cliente do banco')

    def checarConta(self):
        ...

    def checarAgencia(self):
        ...


itau = Banco()
caixa = Banco()
santander = Banco()

conta1 = ContaPoupanca(1, 202, 1553.00)
conta2 = ContaCorrente(1, 109, 3450.50)
conta3 = ContaPoupanca(3, 311, 1553.00)


cliente1 = Cliente('Junior', 20)
cliente2 = Cliente('Ana', 32)
cliente3 = Cliente('Rafael', 62)

cliente1.conta = itau
cliente2.conta = caixa
cliente3.conta = santander

itau.conta = conta1
caixa.conta = conta2
santander.conta = conta3

itau.cliente = cliente1
caixa.cliente = cliente2
santander.cliente = cliente3

print(cliente1.conta.sacar(100))