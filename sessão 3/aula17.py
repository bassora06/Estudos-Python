class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibirDetalhes(self):
         print(f'\nNome: {self.nome}')
         print(f'Sobrenome: {self.sobrenome}')
    


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
   def __init__(self, nome, sobrenome, ra):
       super().__init__(nome, sobrenome)
       self.ra = ra

   def exibirDetalhes(self):
        retorno = super().exibirDetalhes()
        print(f'RA: {self.ra}')
        return retorno


# c1 = Cliente('Lucas', 'Bassora')
# c1.exibirDetalhes()
a1 = Aluno('Ana','Troiano', 1234)
a1.exibirDetalhes()