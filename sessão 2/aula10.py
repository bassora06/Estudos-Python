
def criarSaudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

bomDia = criarSaudacao('Bom dia')
boaNoite = criarSaudacao('Boa noite')


for nome in ['Lucas', 'Samira', 'Matheus', 'João']:
    print(bomDia(nome))