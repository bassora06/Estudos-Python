from abc import ABC

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @ABC.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')
    



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