class MyList():
    def __init__(self):
        self._data = {}
        self._index = 0

    
    def append(self, valor):
        self._data[self._index] = valor
        self._index += 1


lista = MyList()
lista.append('maria')
lista.append('Junior')


print(lista._data)
