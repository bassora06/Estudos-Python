class Pessoa():
    ano = 2023

    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def pessoaAnonima(cls, idade):
        return cls('Anonima', idade)


    @classmethod
    def pessoaDe50Anos(cls, nome):
        return cls(nome, 50)

 
p1 = Pessoa('João', 45)
p2 = Pessoa.pessoaDe50Anos('lucas')
p3 = Pessoa.pessoaAnonima(45)

print(p2.nome, p2.idade)
print(p1.nome, p1.idade)
print(p3.nome, p3.idade)

