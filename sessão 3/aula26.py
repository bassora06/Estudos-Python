class A():
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        instancia.x = 256
        return instancia
    
    def __init__(self, y):
        self.y = y
        print('Eu sou o init')
    
    def __repr__(self):
        return f'A({self.x}, {self.y})'


a = A(21)
print(a)
