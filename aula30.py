"""
CONSTANTE = "Variavéis" que não vão mudar
muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60 # velocidade atual do carro
local_carro = 99 # local em que o caqrro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está 
RADAR_RANGER = 1 # A distância onde o radar pega

velocidade_car_rd_1 = velocidade > RADAR_1
 
local_ranger_menor = local_carro >= (LOCAL_1 - RADAR_RANGER)
local_ranger_maior = local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_passou_rd_1 = local_ranger_menor and local_ranger_maior
carro_multado_rd_1  = carro_passou_rd_1 and velocidade_car_rd_1

if velocidade_car_rd_1:
    print('Passou da volocidade do radar 1')

if carro_passou_rd_1:
    print('Carro passou no radar 1')

if carro_multado_rd_1:
    print('Foi multado')
else:
    print('Velocidade normal')