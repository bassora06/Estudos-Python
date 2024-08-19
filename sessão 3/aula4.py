class Animal():
    def __init__(self, tipo, alimentacao, patas, peso):
        self.tipo = tipo
        self.alimentacao = alimentacao
        self.patas = patas
        self.peso = peso

    def imprimir(self):
        print(f'Tipo: {self.tipo}')
        print(f'Alimentação: {self.alimentacao}')
        print(f'Patas: {self.patas}')
        print(f'Peso: {self.peso}')

an1 = Animal("Mamifero", "carnivoro", "4", "400.00")
an1.imprimir()

    