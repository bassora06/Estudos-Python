class ContextManager():
    def __init__(self, caminhoArquivo, modo):
        self.caminhoArquivo = caminhoArquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abindo arquivo')
        self._arquivo = open(self.caminhoArquivo, self.modo, encoding='utf8')
        return self._arquivo
    

    def __exit__(self, classException_, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()
        print('Exit')

instancia = ContextManager('arquivo222.txt', 'w')

with instancia as arquivo:
    arquivo.write('Bem vindo a aula de context manager\n')
    arquivo.write('Aula 27\n')
    arquivo.write('Aluno: Lucas')
    print('With', arquivo)