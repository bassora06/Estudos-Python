from aula37M import soma # executa oque tem no módulo aula37M pois foi importado
import aula37M
import sys

print('Este módulo se chama', __name__) 
print(f'A soma deu {soma(2, 4)}') # com import do método
print(aula37M.soma(5, 5)) # com import normal

# print(*sys.path, sep='\n') # *sys.path pega os caminhos que está salvo a aula 32 juntamente com as bibliotecas e etc