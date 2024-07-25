class Carro():
    def __init__(self, nome):
        self.nome = nome
        self.fabricantes = []
        self.motores = []

    def inserirFabricante(self, nome):
        self.fabricantes.append(Fabricante(nome))

    def inserirMotor(self, nome):
        self.motores.append(Motor(nome))

    def exibirDetalhes(self):
        for fabricante in self.fabricantes:
            for motor in self.motores:
                print(f'Carro: {self.nome} \nFabricante: {fabricante.nome} \nMotor {motor.nome}\n--------------------------------')

class Motor():
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def inserirCarros(self, nome):
        self.carros.append(Carro(nome))

    def exibirMotor(self, carros):
        print(f'O motor: {self.nome} está presente nos seguintes carros: ')
        for carro in carros:
            print(carro)


class Fabricante():
    def __init__(self, nome):
        self.nome = nome


cr = Carro('Uno')
cr.inserirFabricante('Fiat')
cr.inserirMotor('1.6 flex')
cr.exibirDetalhes()

cr1 = Carro('Civic')
cr1.inserirFabricante('Honda')
cr1.inserirMotor('2.6 turbo')
cr1.exibirDetalhes()

cr2 = Carro('Mustang')
cr2.inserirFabricante('Ford')
cr2.inserirMotor('5.0 turbo')
cr2.exibirDetalhes()

