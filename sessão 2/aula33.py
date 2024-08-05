try:
    lista = [1, 2, 3]
    a = 10
    b = 2
    c = a / b
    print(lista[0])
except( NameError, ZeroDivisionError, IndexError) as error:
    print('Erro: ', error)
    print('Tipo: ', error.__class__.__name__)
