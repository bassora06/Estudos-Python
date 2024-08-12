estados = ['SP', 'MG', 'BA', 'RJ']
cidades = ['Ubatuba', 'Belo Horizonte', 'Salvador']
lista = []


def zipper(cidades, estados):

    if len(estados) < len(cidades):
        for i in range(len(estados)):
            res = f'{estados[i]} {cidades[i]}'
            lista.append((res))
        return lista
    
    for i in range(len(cidades)):
        res = f'{estados[i]} {cidades[i]}'
        lista.append((res))
    return lista
   
zipper(estados, cidades)


print(lista)