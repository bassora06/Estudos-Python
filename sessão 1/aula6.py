entra = input("Digite [E]ntrar ou [S]air: ")
senha = input("Digite sua senha: ")

senha_correta = '123456'

if entra == 'E' or entra == 'e' and senha == senha_correta:
    print('Login realizado com sucesso')
else:
    print('Saída realizada ou senha incorreta')


print(True and 1 and False)