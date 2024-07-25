import os

continuar = True
lista = []

while continuar:
    string = input('Digite uma fruta pra adicional na lista de frutas: ')
    lista += [string]

    sair = input('Deseja continuar? [s]im ')
    sair.lower

    if sair != 's':
        break
    
os.system('cls')
for frutas in lista:
    print(frutas)



