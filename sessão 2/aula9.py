
def saudacao(msg, nome):    # first class function: Funções que são tratadas como outros tipos de dados comuns
    return f'{msg}, {nome}!'

def executa(funcao, *args): # higher function older: Função que retorna outra função
    return funcao(*args)


funcao = executa(saudacao, 'Bom dia', 'Lucas Bassora da Silva')
print(funcao)