from functools import partial

def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentarValor(valor, porcentagem):
    return round(valor * porcentagem)

def mudaPrecoDeProdutos(produto):
    return {
        **produto,
        'preço': aumentarDezPorCento(produto['preço'])
    }

aumentarDezPorCento = partial(
    aumentarValor,
    porcentagem = 1.1
)



produtos = [
    {'nome':'produto 5', 'preço': 10.00},
    {'nome':'produto 1', 'preço': 22.20},
    {'nome':'produto 3', 'preço': 40.45},
    {'nome':'produto 2', 'preço': 12.50},
    {'nome':'produto 4', 'preço': 110.79},
]

# novosProdutos = [
#     {**p, 'preço': aumentarDezPorCento(p['preço'])}  # **p serve para pegar valores anteriores
#     for p in produtos
# ]

novosProdutos = map(
    mudaPrecoDeProdutos,
    produtos
)

printIter(produtos)
printIter(novosProdutos)
