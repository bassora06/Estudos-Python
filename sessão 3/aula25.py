class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # Mostrar aos desenvolvedores como retornar o objeto
    def __repr__(self):
        className = type(self).__name__
        return f'{className}(x={self.x!r}, y={self.y!r})'
    
    def __add__ (self, other):
        novoX = self.x + other.x
        novoY = self.y + other.y
        return Ponto(novoX, novoY)
    
    def __add__ (self, other):
        novoX = self.x + other.x
        novoY = self.y + other.y
        return Ponto(novoX, novoY)
    
    def __gt__(self, other):
        resultadoSelf = self.x + self.y
        resultadoOther = other.x + other.y
        return resultadoSelf > resultadoOther
    
if __name__ == '__main__':
    p1 = Ponto(4, 5)
    p2 = Ponto(10 , 15)
    p3 = p1 + p2
    print('O p1 é maior q p2', p1 > p2)
    print(p3)
    


    
