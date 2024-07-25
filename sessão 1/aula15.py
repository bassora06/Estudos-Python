frase = 'Seja bem vindo aaaaaa'

i = 0
qtd_apareuceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareuceu_mais_vezes_atual = frase.count(letra_atual )

    if qtd_apareuceu_mais_vezes < qtd_apareuceu_mais_vezes_atual:
        qtd_apareuceu_mais_vezes = qtd_apareuceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" que apareceu "{qtd_apareuceu_mais_vezes}" vezes')