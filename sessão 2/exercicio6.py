produtos = [
    {'nome': 'produto 4', 'preço' : 105.87},
    {'nome': 'produto 2', 'preço' : 22.32},
    {'nome': 'produto 3', 'preço' : 10.11},
    {'nome': 'produto 1', 'preço' : 10.00},
    {'nome': 'produto 5', 'preço' : 69.90},
]

novosProdutos = [
    {**produto, 'preço' : produto['preço'] + (produto['preço'] * 10) / 100} 
    for produto in produtos

]

produtosOrdenadosPorNome = [
    {'nome' : produto['nome'], **produto}
    for produto in produtos
]


produtosOrdenadosPorPreco = sorted(produtos)

# for produto in novosProdutos:
#     for nome, valor in produto.items():
#         print(f'{nome} : {valor}')
#     print()

# for produto in produtosOrdenadosPorNome:
#     for nome, valor in produto.items():
#         print(f'{nome} : {valor}')
#     print()
    

for produto in produtosOrdenadosPorPreco:
    for nome, valor in produto.items():
        print(f'{nome} : {valor}')
    print()
