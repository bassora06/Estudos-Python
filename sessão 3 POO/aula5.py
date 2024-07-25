class Camera():
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if not self.filmando:
            print(f'A {self.nome} está filmando')
            self.filmando = True
        else:
            print(f'A {self.nome} ja está filmando')

    def pararFilmagem(self):
        if not self.filmando:
            print(f'não é possivel parar de filmar pois a {self.nome} não está filmando')
        else:
            print(f'A {self.nome} esta parando de filmar')
            self.filmando = False

    def fotografar(self):
        if not self.filmando:
            print(f'Click a {self.nome} tirou uma foto')
        else:
            print(f'A {self.nome} não pode tirar fotos pois esta filmando')

c1 = Camera('Canon')
c2 = Camera('Nani')

c2.fotografar()



