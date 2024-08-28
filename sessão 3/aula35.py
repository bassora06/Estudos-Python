import enum

class Direcoes(enum.Enum):
    ESQUERDA = 'esquerda'
    DIREITA = 'direita'
    ACIMA = 'acima'
    ABAIXO = 'abaixo'


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para a {direcao.value}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ABAIXO)
mover(Direcoes.ACIMA)
