import sys

iterable = ['oi', 'bom dia', 'tudo bem?']
iterator = iter(iterable)

lista = [n for n in range(10000000)]
generator = (n for n in range(100000000))


print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for i in iterable:
    print(next(iterator))