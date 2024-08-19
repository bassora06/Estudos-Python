def adicionaCliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adicionaCliente('lucas')
adicionaCliente('Joana', cliente1)

cliente2 = adicionaCliente('Luiz')
adicionaCliente('Maria', cliente2)

print(cliente1)
print(cliente2)