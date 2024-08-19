listaDeTarefas = []
listaDesfeita = []

while True:
    print('Comandos: Listar, Desfazer, Refazer')
    comando = input('Digite uma tarefa ou comando: ')
    print()


    if comando == 'listar' or comando =='Listar':
        print('Tarefas:')
        for i in listaDeTarefas:
            print(f'{i}')
    elif comando == 'desfazer' or comando == 'Desfazer':
        if not listaDeTarefas:
            print('Não há itens para desfazer')
        else:
            ultimoItem = len(listaDeTarefas) - 1
            listaDesfeita.append(listaDeTarefas[ultimoItem])
            listaDeTarefas.pop()
    elif comando == 'Refazer' or comando == 'refazer':
            if not listaDesfeita:
                 print('não há itens desfeitos')
            else:
                ultimoItem = len(listaDesfeita) - 1
                listaDeTarefas.append(listaDesfeita[ultimoItem])
                listaDesfeita.pop()
    else:
        listaDeTarefas.append(comando)


