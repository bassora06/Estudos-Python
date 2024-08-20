import os

def listar():
     print('Tarefas:')
     if not listaDeTarefas:
        print('Não há itens na lista de tarefas')
        print()
     else:
        for i in listaDeTarefas:
            print(f'{i}')
        print()

def desfazer():
    if not listaDeTarefas:
        print('Não há itens para desfazer')
    else:
        ultimoItem = len(listaDeTarefas) - 1
        listaDesfeita.append(listaDeTarefas[ultimoItem])
        listaDeTarefas.pop()
    os.system('cls')

def refazer():
    if not listaDesfeita:
        print('não há itens desfeitos')
    else:
        ultimoItem = len(listaDesfeita) - 1
        listaDeTarefas.append(listaDesfeita[ultimoItem])
        listaDesfeita.pop()
    os.system('cls')

listaDeTarefas = []
listaDesfeita = []

while True:
    print('Comandos: Listar, Desfazer, Refazer')
    comando = input('Digite uma tarefa ou comando: ')
    print()


    if comando == 'Listar' or comando =='listar':
        listar()
    elif comando == 'Desfazer' or comando == 'desfazer':
        desfazer()
    elif comando == 'Refazer' or comando == 'refazer':
        refazer()
    else:
        listaDeTarefas.append(comando)
        os.system('cls')


