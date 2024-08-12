listaNumeros1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
listaNumeros2 = [1 ,2 ,3 ,4]
lista = []


def somarListas(lista1, lista2):

    if len(lista1) < len(lista2):
        for i in range(len(lista1)):
            res = lista1[i] + lista2[i]
            lista.append(res)
        return lista
    
    for i in range(len(lista2)):
        res = lista1[i] + lista2[i]
        lista.append(res)
    return lista
   
somarListas(listaNumeros1, listaNumeros2)

print(lista)