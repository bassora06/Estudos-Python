def executar(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criaMultiplicador(multiplicador):
    def multiplicar(valor):
        return valor * multiplicador
    return multiplicar

print('Função de somar:',
    executar(lambda x, y: x + y, 
    4, 5)
)

duplica = executar( lambda m: lambda v: m*v, 4)

print('função de multiplicar: ', duplica(2))

print('Função usando args para somar: ',
    executar(
        lambda *args: sum(args), 2, 3, 4, 5
    )
)
