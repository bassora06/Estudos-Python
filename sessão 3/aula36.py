from dataclasses import dataclass

@dataclass() # init = false, desabilita o init
class Pessoa(): 
    nome: str
    idade: int

    def __post_init__(self): # executado após o init
        self.info = f'Nome: {self.nome} ,Idade: {self.idade}'


p1 = Pessoa('lucas', 18)
print(p1.info)
