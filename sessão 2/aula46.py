from itertools import groupby

alunos = [
    {'nome': 'Lucas', 'Nota': 'A'},
    {'nome': 'Ana', 'Nota': 'B'},
    {'nome': 'Julia', 'Nota': 'A'},
    {'nome': 'João', 'Nota': 'C'},
    {'nome': 'Matheus', 'Nota': 'D'},
    {'nome': 'Eduardo', 'Nota': 'D'},
    {'nome': 'Élise', 'Nota': 'C'},
    {'nome': 'Laura', 'Nota': 'B'},
]

def ordena(aluno):
    return aluno['Nota']

alunosAgrupados = sorted(alunos, key=ordena)
grupos = groupby(alunosAgrupados, key=ordena)

for chave, grupo in grupos:
    print(chave) # Pega o indice armazenado na lista
    for aluno in grupo:
        print(aluno) # mostra quantas vezes ele se repete

