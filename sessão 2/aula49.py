from functools import reduce

produtos = [
    {'nome':'produto 5', 'preço': 10.00},
    {'nome':'produto 1', 'preço': 22.20},
    {'nome':'produto 3', 'preço': 40.45},
    {'nome':'produto 2', 'preço': 12.50},
    {'nome':'produto 4', 'preço': 110.79},
]

def funcaoAcumuladora(acumulador, produto):
    print('Acumulador:', acumulador)
    print('Produto: ', produto['preço'])
    print()
    return acumulador + produto['preço']


total = reduce(
    funcaoAcumuladora,
    produtos,
    0
)

print(f'O total é {total}')


# total = 0

# for p in produtos:
#     total += p['preço']

# print(total)
