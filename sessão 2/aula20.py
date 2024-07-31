
lista = [
    {'Nome': 'Lucas', 'Sobrenome': 'Bassora'},
    {'Nome': 'Ana', 'Sobrenome': 'Carvalho'},
    {'Nome': 'Eloah', 'Sobrenome': 'Faria'},
    {'Nome': 'José', 'Sobrenome': 'Davi'},
]


# lista.sort(key= lambda item: item['Nome'])

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)
    print()

sobrenome = sorted(lista, key=lambda item: item['Sobrenome'])
nome = sorted(lista, key=lambda item: item['Nome'])

exibir(sobrenome)
exibir(nome)