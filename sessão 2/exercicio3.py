    
def duplicar(numero):
    def multiplicarPor2(multiplicador):
        return numero * multiplicador
    return multiplicarPor2

    
def triplicar(multiplicador):
    def multiplicarPor3(numero):
        return numero * multiplicador
    return multiplicarPor3

    
def quadruplicar(multiplicador):
    def multiplicarPor4(numero):
        return numero * multiplicador
    return multiplicarPor4
    

dobro = duplicar(2)
triplicar = triplicar(3)
quadruplicar = quadruplicar(4)
numeros = 2 , 3, 5, 6, 9, 10
valoresDobrados = []
valoresTriplicados = []
valoresQuadriplicados = []

for i in numeros:
    valoresDobrados += [dobro(i)]

for i in numeros:
    valoresTriplicados += [triplicar(i)]

for i in numeros:
    valoresQuadriplicados += [quadruplicar(i)]

print(valoresDobrados)
print(valoresTriplicados)
print(valoresQuadriplicados)
    
    

