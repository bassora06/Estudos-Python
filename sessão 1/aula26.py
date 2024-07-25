frase = 'Olá só que, vamos separar'
lista_Palavras = frase.split(', ')

lista_frases = []

for i, frase in enumerate(lista_frases):
    lista_frases.append(lista_Palavras[i].split())
    print(lista_Palavras[i])


print(lista_Palavras)
print(lista_frases)

frases_unidas = '*'.join(lista_frases)

print(frases_unidas)


