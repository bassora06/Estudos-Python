x, y, *resto = 1, 2, 3, 4

def somar(*args):
    soma = 0

    for n in args:
        soma += n

    return soma

soma = somar(1,2, 3, 4, 5, 3, 2, 23, 41) #passa o retorno da função para variavel e exibe depois
print(soma)