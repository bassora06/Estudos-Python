class Carro():
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def fabricante(self):
        return self._fabricante
    

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    def exibirDetalhes(self):
        print(f'Carro: {self.nome} \nMotor: {self.motor.nome} \nFabricante: {self.fabricante.nome}\n-----------------------------------')
       
    
class Moto():
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._Fabricante = None

    @property
    def fabricante(self):
        return self._fabricante
    

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    def exibirDetalhes(self):
        print(f'Moto: {self.nome} \nMotor: {self.motor.nome} \nFabricante: {self.fabricante.nome}\n-----------------------------------')
       
   
    
    

class Fabricante():
    def __init__(self, nome):
        self.nome = nome


class Motor():
    def __init__(self, nome):
        self.nome = nome


uno = Carro('Uno')
civic = Carro('Civic')
mustang = Carro('Mustang')

m10 = Motor('1.0')
m20 = Motor('2.0')
m50t = Motor('5.0 turbo')
cc250 = Motor('250 Cilindradas')
cc160 = Motor('160 Cilindradas')

fiat = Fabricante('Fiat')
honda = Fabricante('Honda')
ford = Fabricante('Ford')
yamaha = Fabricante('Yamaha')

uno.fabricante = fiat
uno.motor = m10

civic.fabricante = honda
civic.motor = m20

mustang.fabricante = ford
mustang.motor = m50t

uno.exibirDetalhes()
civic.exibirDetalhes()
mustang.exibirDetalhes()

fz25 = Moto('FZ25')
fz25.fabricante = yamaha
fz25.motor = cc250

titan160 = Moto('Titan')
titan160.fabricante = honda
titan160.motor = cc160

fz25.exibirDetalhes()
titan160.exibirDetalhes()











