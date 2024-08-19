import os

caminhoArquivo = 'C:\\Users\\pc\\Documents\\meuPc\\Estudos-Python-Modulo\sessão 2\\'
caminhoArquivo += 'arquivo.txt'

# arquivo = open(caminhoArquivo, 'r')

# arquivo.close()

with open(caminhoArquivo, 'w+', encoding='utf-8')as arquivo:
    arquivo.write('atenção\n')
    arquivo.write('Vagabundo\n') #escreve no arquivo
    # arquivo.seek(0, 0)# mecher o cursos do arquivo
    arquivo.writelines(
        ('Linha 1\n', 'Linha 2\n', 'Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read()) # consigo ler o arquivo após modificar por conta do +

print('#' * 10, '\n')

with open(caminhoArquivo, 'r')as arquivo:
    print(arquivo.read()) # le o arquivo
    print('Aqui esta o arquivo')

# os.remove(caminhoArquivo)
print('Arquivo removido')
os.rename(caminhoArquivo, 'bem vindo.txt') # renomeia o arquivo
    

