import pprint
# lista = []

# # Adicionando itens a lista de forma normal
# for numero in range(10):
#     lista.append(numero)

# # print(lista)

# # List comprehension
# lista = [numero for numero in range(10)]
# print(lista)

# # List comprehension usado de outras formas
# lista2 = [numero * 3 for numero in range(10)]
# print(lista2)

def p(valor):
    print(*valor, sep='\n')

produtos = [
    {'nome': 'p1', 'preço': 10},
    {'nome': 'p2', 'preço': 20},
    {'nome': 'p3', 'preço': 30}
]

novosProduto = [
    {**produto, 'preço' : produto['preço'] * 1.05} 
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    if produto['preço'] >= 20

]

p(novosProduto)
