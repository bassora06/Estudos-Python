lista = []

for i in range(3):
    for x in range(3):
        lista.append((i, x))

print(lista)

lista = [
    (i, x)
    for i in range(3)
    for x in range(3)
]

print(lista)

lista = [
    [(letra) for letra in 'Lucas']
    for x in range(4)
]

print(lista)