def parametrosDecorador(nome):

    def decorador(func):

        print('decorador:', nome)

        def novaFuncao(*args, **kwargs): # inner function ou aninhada

            print('Aninhada')
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        
        return novaFuncao
    
    return decorador


@parametrosDecorador('soma') # python decora automaticamente
def soma(x, y): # função sendo decorada
    return x + y
    




dezMaisCinco = soma(10, 5)


print(dezMaisCinco)

    
