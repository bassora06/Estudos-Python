lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2, 3), {1, 2, 3}, {'nome':'Lucas'}
]

for item in lista:
    if isinstance(item, str):
        print(item.upper())

    if isinstance(item, int):
        print(item)

    if isinstance(item, float):
        print(item * 2)
