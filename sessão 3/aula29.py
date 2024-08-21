def adicionaRepr(cls):
    def myRepr(self):
        className = self.__class__.__name__
        classDict = self.__dict__
        classRepr = f'{className}({classDict})'
        return classRepr
    cls.__repr__ = myRepr
    return cls


@adicionaRepr
class Time():
    def __init__(self, nome):
        self.nome = nome



@adicionaRepr
class Planeta():
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
argentina = Time('Argentina')


terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(argentina)
print(terra)
print(marte)
        