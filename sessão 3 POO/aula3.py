class pessoa():
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def falar(self):
        print(f'{self.nome}: bla bla bla')


p1 = pessoa('Lucas', '38105603837', '18')

print(p1.nome, p1.cpf, p1.idade)
p1.falar()