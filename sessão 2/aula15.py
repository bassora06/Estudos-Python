p1 = {
    'nome': 'Lucas',
    'sobrenome': 'Bassora'
}

# print(p1['nome'])
# print(p1.get('nome', 'não existe um nome'))

#p1.pop('nome') # remove a chave escolhida no parametro
# p1.popitem() # romeve a ultima chave
print(p1)

p1.update({ # forma 1 de usar o update para atualizar dados
    'nome': 'novo valor',
    'sobrenome': 'carvalho'
})

print(p1)

p1.update(nome= 'Lucas Vassora', sobrenome='Cavaleiro') # forma 2 de usar o update para atualizar dados
print(p1)