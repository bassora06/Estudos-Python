s1 = {1 ,2 ,3}
s2 = {3, 4, 5}

s3 = s1 | s2 # Com o pipe ele pega todos os valores dos 2 sets 
s4 = s1 & s2 # com o e comercial ele pega apenas o valor que ambos tem em comum
s5 = s1 - s2 # Pega os valores que estão presentes apenas no primeiro set
s6 = s1 ^ s2 # Pega os valores que ambos não tem em comum

print(s3)
print(s4)
print(s5)
print(s6)