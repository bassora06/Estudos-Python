# variaves dentro de funções são locais, e fora são globais

x = 'Essa variavel é global'

def escopo():
    x = 1
    y = 'Essa variavel é local'
    print(y)

escopo()
print(x)