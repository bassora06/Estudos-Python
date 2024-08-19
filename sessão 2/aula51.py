caminhoArquivo = 'C:\\Users\\pc\\Documents\\meuPc\\Estudos-Python-Modulo\\sessão 2\\'
caminhoArquivo += 'arquivo.txt'

# arquivo = open(caminhoArquivo, 'r')

# arquivo.close()

with open(caminhoArquivo, 'w+')as arquivo:
    arquivo.write('Seja bem vindo\n')
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
    

