def decoradora(func):

    print('decoradora')

    def aninhada(*args, **kwargs): # inner function ou aninhada

        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    
    return aninhada
    

    
@decoradora # python decora automaticamente
def soma(x, y): # função sendo decorada
    return x + y
    


dezMaisCinco = soma(10, 5)
print(dezMaisCinco)

    
