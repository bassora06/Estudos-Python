from contextlib import contextmanager


@contextmanager
def myOpen(caminhoArquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminhoArquivo, modo, encoding='utf8')
        yield arquivo 
    finally:
        print('Fechando arquivo')
        arquivo.close()


with myOpen('arquivo123.txt', 'w') as arquivo:

    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With', arquivo)

