    
def criarMultiplicacao(numero):
    def multiplicar(multiplicador):
        return numero * multiplicador
    return multiplicar

    
    

dobro = criarMultiplicacao(2)
triplicar = criarMultiplicacao(3)
quadruplicar = criarMultiplicacao(4)
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
    
    

