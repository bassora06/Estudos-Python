#   modificadores de acesso
#   publico sem underline
#   protected 1 underline
#   private 2 underlines

class Foo():

    def __init__(self):
        self.public     = 'Esse atributo é publico'
        self._protegido = 'Esse atributo é protegido'
        self.__privado  = 'Esse atributo é privado'


    def metodoPublico(self):
        print(f.__privado)
        print(f._protegido)
        return 'Metodo publico'
    
    def _metodoProtegido(self):
        return 'Metodo protegido'
    

    def __metodoPrivado(self):
        return 'Metodo Privado'
    

f = Foo()
print(f.public)
print(f.metodoPublico())
print(f._metodoProtegido())
#print(f._Foo__metodoPrivado()) # muda pelo método mangling ou seja, não deve acessar