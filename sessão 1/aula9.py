velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 102
RADAR_RANGE = 1

velocidade_carro_passou_radar = velocidade > RADAR_1
multar_carro = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar:
    print('A velocidade excedeu a permitina na pista')

if multar_carro and velocidade_carro_passou_radar:
    print('Velocidade do carro passou do radar')