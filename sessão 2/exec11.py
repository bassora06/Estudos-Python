import os
import json

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
    criarJson()

def refazer():
    if not listaDesfeita:
        print('não há itens desfeitos')
    else:
        ultimoItem = len(listaDesfeita) - 1
        listaDeTarefas.append(listaDesfeita[ultimoItem])
        listaDesfeita.pop()
    criarJson()

def criarJson():
    with open('tarefas.json', 'w', encoding='utf-8')as arquivo:
        json.dump(listaDeTarefas, arquivo, ensure_ascii=False ,indent=3)


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
    elif comando =='cls':
        os.system('cls')
    else:
        listaDeTarefas.append(comando)
        os.system('cls')
        criarJson()




