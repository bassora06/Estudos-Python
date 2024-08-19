numeroDuplicado = 0 
listaDeNumeros = [[1, 2, 3, 3, 2, 1],
                  [1, 2, 3, 4, 5, 6],
                  [2, 2, 3 ,3 ,4 ,4],
                  [5, 6, 7, 8, 7, 5],
                  [10, 10, 12, 13, 43]]



def acharNumeroDuplicado(lista):
    listaDeValidacao = set()
    primeiroDuplicado = -1
    for numero in lista:
        if numero in listaDeValidacao:
            primeiroDuplicado = numero
            break
        
        listaDeValidacao.add(numero)
    return primeiroDuplicado
    
    
       
       

for lista in listaDeNumeros:
    print(lista, acharNumeroDuplicado(lista))

