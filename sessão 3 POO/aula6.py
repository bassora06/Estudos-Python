class Pessoa():
    anoAtual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNascimento(self):
         anoNascimento = Pessoa.anoAtual - self.idade
         return anoNascimento


p1 = Pessoa('Julia', 53)
p2 = Pessoa('Lucas', 19)

p1.nome = 'João'
p1.__dict__["outra"] = 'coisa'
p1.__dict__['nome'] = 'Joao'
del p1.__dict__['nome']

print(p1.__dict__)
print(vars(p1))
print(p1.outra)
