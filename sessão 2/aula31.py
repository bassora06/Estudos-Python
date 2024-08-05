def gen1(gen=None):
    print('iniciou gen1')
    if gen is not None:
        yield from gen()
    yield 1
    yield 2
    yield 3
    print('terminou gen1')

def gen2():
    print('começou gen2')
    yield 4
    yield 5
    yield 6
    print('Terminou gen2')

def gen3():
    print('Começou gen3')
    yield 7
    yield 8
    yield 9
    print('Terminou gen3')

g1 = gen1(gen2)
g2 = gen1(gen3)

for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()



