def decoratorsFactory(a=None, b=None, c=None):

    def functionsFactory(func):

        print('decoradora')

        def aninhada(*args, **kwargs): # inner function ou aninhada

            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        
        return aninhada
    
    return functionsFactory


@decoratorsFactory(1, 2, 3) # python decora automaticamente
def soma(x, y): # função sendo decorada
    return x + y
    


decoradora = decoratorsFactory()
multiplica = decoradora(lambda x , y: x * y)

dezMaisCinco = soma(10, 5)
dezVezesCinco = multiplica(10, 5)

print(dezMaisCinco)
print(dezVezesCinco)

    
