class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserirEndereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def exibirEndereco(self):
        for endereco in self.enderecos:
            print(f'Morador: {self.nome} \nRua: {endereco.rua} \nNumero: {endereco.numero}\n-------------------------------')


class Endereco():
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cli1 = Cliente('lucas')
cli2 = Cliente('Ana Carolina')
cli2.inserirEndereco('Amoras', 2341)
cli1.inserirEndereco('Manoel Antonio vilela', 21)
cli1.exibirEndereco()
cli2.exibirEndereco()

