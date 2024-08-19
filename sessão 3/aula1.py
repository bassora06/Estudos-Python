# instancia = cli, atributos. O self é a instancia e o restante os atributos da classe
#A classe tem uma função init que inicializa os atributos da classe

class Cliente:
    def __init__(self, nome, sobrenome): 
        self.nome = nome
        self.sobrenome = sobrenome

    



cli = Cliente('Luiz', 'Otávio')
cli2 = Cliente('Lucas', 'Bassora')

print(cli.nome, cli.sobrenome)
print(cli2.nome, cli2.sobrenome)
