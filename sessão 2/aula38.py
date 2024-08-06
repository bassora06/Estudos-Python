import importlib
import aula38M

print(aula38M.variavel)

for i in range(10):
    importlib.reload(aula38M)

print('fim')

# Módulo do python pode ser carregado apenas uma vez, por isso foi utilizado o importlib.reload para recarregar
# o móludo