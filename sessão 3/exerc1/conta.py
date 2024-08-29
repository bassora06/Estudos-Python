import abc

class Conta(abc.ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor):
        valorPosSaque = self.saldo - valor

        if valorPosSaque >= 0:
            self.saldo -= valor
            self.detalhes(f'O saque foi relizado com sucesso')
            return self.saldo
        self.detalhes(f'O saque não pode ser concluido: {valor} R$')
        

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'O valor depositado foi de: {valor} R$')

    def detalhes(self, msg=''):
        print(f'{msg}\nSaldo: {self.saldo:.2f} R$')
        print()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valorPosSaque = self.saldo - valor

        if valorPosSaque >= 0:
            self.saldo -= valor
            self.detalhes(f'O saque foi relizado com sucesso')
            return self.saldo
        self.detalhes(f'O saque não pode ser concluido, saque realizado: {valor} R$')

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=0):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        valorPosSaque = self.saldo - valor
        self.limite = -self.limite

        if valorPosSaque >= self.limite:
            self.saldo -= valor
            self.detalhes(f'O saque foi relizado com sucesso')
            return self.saldo
        self.detalhes(f'Seu limite é de: {self.limite}\nO saque não pode ser concluido, saque realizado: {valor} R$')


if __name__ == '__main__':
    # cp1 = ContaPoupanca(1, 2, 1000.40)
    # cp1.sacar(1100)
    # cp1.depositar(100)
    # print('###################')
    cc1 = ContaCorrente(1, 2, 200, 100)
    cc1.sacar(310)

        
