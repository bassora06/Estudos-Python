def soma(x, y):
    return x + y

def multiplica(x , y):
    return x * y


def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


somaComCinco = executa(soma, 5)
multiplicaPorDez = executa(multiplica, 10)

print(somaComCinco(10))