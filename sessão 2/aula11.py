
pessoa = {
    'Nome': 'Lucas Bassora',
    'Sobrenome' : 'da Silva',
    'Altura' : 1.78,
    'Peso': 70,
    'enderecos': [
        {'Rua' : 'Manoel Antônio Vilela', 'Numero': 21},
        {'Rua' : 'Rua das Ipirangas', 'Numero': 43}
    ]
}

for key in pessoa:
    print(f'{key} : {pessoa[key]}')