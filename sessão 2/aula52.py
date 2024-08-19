import json

pessoa = {
    'nome' : 'Lucas Bassora',
    'sobrenome': 'da Silva',
    'endereços': [
        {'Rua': 'R1', 'numero': '21'},
        {'Rua': 'R2', 'numero': '32'},
    ],
    'altura': 1.78,
    'numerosPreferidos': (2, 4, 5, 6, 10),
    'dev': True,
    'Nada': None,
}

# with open('informacoes.json', 'w', encoding='utf-8')as arquivo:
#     json.dump(
#             pessoa, 
#             arquivo, 
#             ensure_ascii=False,
#             indent=2)

with open('informacoes.json', 'r', encoding='utf-8')as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(pessoa['nome'])