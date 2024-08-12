from itertools import combinations, permutations, product

def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['lucas', 'joão', 'maria', 'ana']

camisetas = [['preta', 'branca'],
             ['P', 'M', 'G', 'GG'],
             ['Masculino', 'Feminino']]


printIter(combinations(pessoas, 2))
printIter(permutations(pessoas, 2))
printIter(product(*camisetas))