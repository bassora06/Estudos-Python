caminhoArquivo = 'C:\\Users\\pc\\Documents\\meuPc\\Estudos-Python-Modulo\\sessão 2\\arquivo.txt'
caminhoArquivo = 'arquivo.txt'

# arquivo = open(caminhoArquivo, 'r')

# arquivo.close()

with open(caminhoArquivo, 'w'):
    print('Olá mundo')
    print('arquivo fechado')

