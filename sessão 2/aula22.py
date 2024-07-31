# a, b = 1, 2
# a, b = b, a

# print(a, b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Bassora'
}

dadosDaPessoa = {
    'idade' : 19,
    'altura': 1.78
}

# (a1, a2), (b1, b2) = pessoa.items()

# print(f'{a1}: {a2}\n{b1}: {b2}')

# KWARGS são argumentos nomeados como por exemplos itens de dicionários

pessoaCompleta = {**pessoa, **dadosDaPessoa}

for chave, valor in pessoaCompleta.items():
    print(f'{chave} : {valor}')
