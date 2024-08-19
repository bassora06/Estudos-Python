class Carro():
    def __init__(self, marca, modelo, motor, cor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self. cor = cor

    def acelerar(self):
        print(f'{self.modelo} está acelerando, katchau')


c1 = Carro('Ford', 'Mustang', '5.0 turbo', 'Laranja')
c2 = Carro('Chevrolet', 'Cobalt', '1.6 flex', 'Prata')

print("Marca______Modelo_______Motor______Cor")
print(f'{c1.marca}      {c1.modelo}     {c1.motor}   {c1.cor}')
print(f'{c2.marca}      {c2.modelo}     {c2.motor}   {c2.cor}')

c1.acelerar()
c2.acelerar()