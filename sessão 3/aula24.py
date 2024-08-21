class Ponto():
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # Apenas retornar como string
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Mostrar aos desenvolvedores como retornar o objeto
    def __repr__(self):
        className = type(self).__name__
        return f'{className}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
    
# p1 = Ponto(4, 5)
p2 = Ponto(10 , 15, 'Ola')

print(p2)
# print(f'{p1!r}')
print(repr(p2))
    


    
