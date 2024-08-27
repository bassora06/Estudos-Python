def soma(x: int | float, y: int | float) -> int | float:
    """
    Está função recebe 2 parametros
    x: pode ser int ou float
    y: pode ser int ou float
    e o retorno por ser int ou float
    """

    return x + y


def multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None
) -> int | float:
    if z == None:
        return x * y
    return x * y * z

"""
Multiplica x e y
caso z não seja none ele multiplica o z também
"""


soma = soma(3.6, 4)
print(soma)

multiplicar = multiplica(3, 4, 6)
print(multiplicar)