def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()

def filtrarProduto(produto):
    return produto['preço'] > 20



produtos = [
    {'nome':'produto 5', 'preço': 10.00},
    {'nome':'produto 1', 'preço': 22.20},
    {'nome':'produto 3', 'preço': 40.45},
    {'nome':'produto 2', 'preço': 12.50},
    {'nome':'produto 4', 'preço': 110.79},
]

# novosProdutos = [
#     p for p in produtos
#     if p['preço'] >= 20
# ]

novosProdutos = filter(
    filtrarProduto, 
    produtos
)

printIter(produtos)
printIter(novosProdutos)
