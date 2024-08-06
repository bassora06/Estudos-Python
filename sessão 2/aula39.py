# import sys
# from aula39Package import modulo
# from aula39Package.modulo import soma
# import aula39Package.modulo
# from aula39Package.modulo import * # má prática

# print(__name__)
# print(modulo.soma(2, 3))
# print(soma(3, 4))
# print(aula39Package.modulo.soma(3, 4))
# print(variavel)
# print(*sys.path, sep='\n')

from aula39Package import modulo, moduloB

print(__name__)
moduloB.falaOi()