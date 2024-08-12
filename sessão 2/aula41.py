def criarFuncao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            eString(arg)

        resultado = funcao(*args, **kwargs)
        print('vou te decorar')
        print('Função decoradora')
        return resultado
    return interna

def eString(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser string')
    

    
@criarFuncao
def invertString(string):
    return string[::-1]
    


invertida = invertString('Lucas')
print(invertida)

    
