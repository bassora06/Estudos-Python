class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever():
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'A {self.nome} está escrevendo'

escritor = Escritor('Lucas')
pincel = FerramentaDeEscrever('Pincel') #Estanciando classe ferramenta e dando um nome
escritor.ferramenta = pincel # Dizendo que o atributo ferramenta do escritor é a classe estanciada pincel

print(pincel.escrever()) # printa o escrever da classe pincel
print(escritor.ferramenta.escrever()) #faz o mesmo porém dizendo para a ferramenta da classe escritor escrever