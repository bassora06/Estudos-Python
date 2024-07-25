class Veiculo:
    def __init__(self, nome, marca, motor):
        self.nome = nome
        self.marca = marca
        self.motor = motor

    def exibirDetalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Marca: {self.marca}')
        print(f'Motor: {self.motor}')


class Carro(Veiculo):
    def __init__(self, nome, marca, motor, portaMala):
        super().__init__(nome, marca, motor)
        self.portaMala = portaMala

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print(f'Porta malas: {self.portaMala}\n------------------------------------------------------')


class Moto(Veiculo):
    def __init__(self, nome, marca, motor, pesinho):
        super().__init__(nome, marca, motor)
        self.pesinho = pesinho

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print(f'Pesinho: {self.pesinho}\n------------------------------------------------------')


class Caminhao(Veiculo):
    def __init__(self, nome, marca, motor, capacidadeCarga):
        super().__init__(nome, marca, motor)
        self.capacidadeCarga = capacidadeCarga

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print(f'Capacidade de carga: {self.capacidadeCarga}\n------------------------------------------------------')


c1 = Carro('Civic', 'Honda', '2.6 Turbo', '5 Litros')
c1.exibirDetalhes()

m1 = Moto('FZ25', 'Yamaha', '250 Cilindrdas', 1)
m1.exibirDetalhes()

ca1 = Caminhao('Não sei', 'Iveco', '3.0', 7000.50)
ca1.exibirDetalhes()
