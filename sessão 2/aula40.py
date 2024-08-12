# def fora(x):
#     a = x

#     def dentro():
#         print(locals())
#         return a
#     return dentro


# dentro = fora(10)
# dentro2 = fora(20)

# print(dentro())
# print(dentro2())

def concatenar(stringInicial):
    valorFinal = stringInicial

    def interna(valorConcatenar=''):
        nonlocal valorFinal
        valorFinal += valorConcatenar
        return valorFinal
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)