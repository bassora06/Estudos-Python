s1 = set()
s1.add(1)
l1 = [1 ,2 ,3 ,4 ,5, 1 ,2 ,3]

for i in l1:
    s1.add(i)

print(s1)
# s1.clear() # Limpa o set
# print(s1)
s1.update((11, 'Olá mundo')) # atualiza os valores
print(s1)
s1.discard(11) #descarta 1 item dentro do set
print(s1)