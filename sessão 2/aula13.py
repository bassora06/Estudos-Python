pessoa = {
    'nome': 'Lucas Bassora',
    'sobrenome': 'da Silva',
    'Idade': 14,
    'Peso': 23.43,
    'Idade':23
}

# print(len(pessoa)) # Mostra a quantidade de chaves

# print('\nAqui mostra os nomes das chaves: ') 
# for i in list(pessoa.keys()):# Mostra os nomes das chaves
#     print(i)

# print('\nAqui mostra os valores das chaves: ')
# for i in list(pessoa.values()): # Mostra o valor das chaves
#     print(i)


# print('\nAqui mostra as chaves e os valores')
# for i in list(pessoa.items()):
#     print(i)

pessoa.setdefault('idade', 'Não existe')

print(pessoa['idade'])

# for chave, valor in pessoa.items():
#     print(f'{chave} : {valor}')



