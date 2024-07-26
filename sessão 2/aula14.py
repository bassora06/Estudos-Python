d1 = {
    'nome' : 'Lucas Bassora',
    'Idade' : 23,
    'Lista' : [1, 3, 4, 5]
}

d2 = d1.copy()

d2['nome'] = 'Matheus Jesus'
d2['Lista'] = [2, 4, 5, 6]

print(f'{d1}\n{d2}')