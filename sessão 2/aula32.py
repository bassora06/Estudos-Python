try:
    lista = [1, 2, 3]
    a = 10
    b = 2
    c = a / b
    print(lista[2])
except ZeroDivisionError:
    print('Erro: Divisão com zero')
except NameError:
    print('Nome de variável não definido')
except IndexError:
    print('Lista não possui essa quantidade de indíces')