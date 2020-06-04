'''
DESAFIO 091

Crie um programa onde 4 JOGADORES joguem um DADO e tenham RESULTADOS ALEATÓRIOS.
GUARDE esses RESULTADOS em um DICIONÁRIO. No final, coloque esse dicionário em
ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no DADO.
'''
# ================ MODELO CRIADO ========================================================================
from random import randint
from time import sleep

jogadores = {'Darlan': randint(1, 6), 'Deivid': randint(1, 6),
             'Fagner': randint(1, 6), 'Kalisson': randint(1, 6)
             }

print('Valores sorteados:')
for item in jogadores:
    print(f'    O jogador {item} tirou {jogadores[item]}')
    sleep(.5)
print('='*40)
sleep(1)
print('Colocação dos jogadores:')
cont = 1
for c in range(1):
    for item in sorted(jogadores, reverse=True, key=jogadores.get):
        print(f'    em {cont}ª lugar {item}')
        sleep(1)
        cont += 1

# ================ MELHORIA DO CÓDIGO ===================================================================

# ================ ANÁLISE DO CÓDIGO ====================================================================

# ================ MODELO CURSO EM VIDEO ================================================================
