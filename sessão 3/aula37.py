from collections import namedtuple

Carta = namedtuple('carta', ['valor', 'Naipe'])

asEspadas = Carta('A', 'Espadas')

print(asEspadas.valor, asEspadas.Naipe)