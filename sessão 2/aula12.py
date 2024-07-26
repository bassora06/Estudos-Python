pessoa = {}

sobrenome = 'sobrenome'

pessoa['nome'] = 'Lucas Bassora'
pessoa[sobrenome] = 'da Silva'

print(pessoa)


pessoa[sobrenome] = 'Carvalho'

print(pessoa)
del pessoa['sobrenome']
print(pessoa)

print(pessoa.get('nome'))

if pessoa.get('sobrenome') is None:
    print('Não existe sobrenome')
else:
    print('Existe um sobrenome')

