# def recursiva(inicio=0, fim= 10):
#     print(inicio, fim)
    
#     if inicio >= fim:
#         return fim

#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

def fatorial(numero):

    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)


print(fatorial(5))