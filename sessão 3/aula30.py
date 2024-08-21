def myRepr(self):
        className = self.__class__.__name__
        classDict = self.__dict__
        classRepr = f'{className}({classDict})'
        return classRepr

def adicionaRepr(cls):
    cls.__repr__ = myRepr
    return cls


@adicionaRepr
class Time():
    def __init__(self, nome):
        self.nome = nome

def myPlanet(metodo):
    def interno(self, *args, **kwargs):
          resultado = metodo(self, *args, **kwargs)

          if 'Terra' in resultado:
               return 'você está em casa'
          return 'Você é um alien'
    
    return interno


@adicionaRepr
class Planeta():
    def __init__(self, nome):
        self.nome = nome

    @myPlanet
    def speakName(self):
         return f'o planeta é {self.nome}'


brasil = Time('Brasil')
argentina = Time('Argentina')


terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(argentina)
print(terra)
print(marte)

print(terra.speakName())
print(marte.speakName())
        