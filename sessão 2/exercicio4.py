import time
import os

perguntas = [
    {
        'pergunta' : 'Quanto é 5*5?',
        'opções' : [10, 34, 25, 30],
        'resposta' : '25'
    },
    {
        'pergunta' : 'Quanto é 25 + 50?',
        'opções' : [100, 45, 20, 75],
        'resposta' : '75'
    },
    {
        'pergunta' : 'Quanto é 100 * 3 - 2?',
        'opções' : [298, 295, 299, 297],
        'resposta' : '298'
    },
    {
        'pergunta' : 'Quanto é 34 + 10 / 2?',
        'opções' : [10, 24, 22, 26],
        'resposta' : '22'
    },
    {
        'pergunta' : 'Quanto é 1024 * 5?',
        'opções' : [5102, 4387, 5120, 8343],
        'resposta' : '5120'
    },
    {
        'pergunta' : 'Quanto é 94 * 3 + 5',
        'opções' : [239, 271, 142, 287],
        'resposta' : '287'
    },
    {
        'pergunta' : 'Quanto é 8 * 6 * 12?',
        'opções' : [576, 513, 642, 563],
        'resposta' : '578'
    },
    {
        'pergunta' : 'Quanto é 66 + 5 + 7 * 2?',
        'opções' : [145, 156, 143, 144],
        'resposta' : '156'
    },
]

pontos = 0
print('Responda as seguintes questões para pontuar')

for i in range(8):
    print(perguntas[i]['pergunta'])
    print(perguntas[i]['opções'])
    resposta = input('Digite uma resposta: ')

    if resposta == perguntas[i]['resposta']:
        pontos += 1
        print('resposta correta')
        time.sleep(2)
        os.system('cls')
    else:
        print('resposta incorreta❌')
        time.sleep(2)
        os.system('cls')

print(f'fim de jogo você marcou: {pontos}/8 pontos')
