produto = {
    'nome' : 'caneta azul',
    'preço' : 3.50,
    'categoria' : 'escritório'
}

dc = {
    chave : valor * 5
    if isinstance(valor, (float, int)) else valor.upper()
    for chave, valor 
    in produto.items()
    if chave != 'categoria' # exibe todos diferente de categoria
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc = {
    chave : valor 
    for chave, valor in lista
}

print(dc)

s1 = {i ** i for i in range(10)}
print(set(range(10)))
print(s1)