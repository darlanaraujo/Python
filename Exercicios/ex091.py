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
    sleep(.7)
print('='*40)
sleep(1.5)

print('Colocação dos jogadores:')
sleep(1)
cont = 1
for c in range(1):
    for item in sorted(jogadores, reverse=True, key=jogadores.get):
        print(f'    {cont}ª lugar {item} com {jogadores[item]}')
        sleep(1)
        cont += 1

# ================ MELHORIA DO CÓDIGO ===================================================================from random import randint
'''from time import sleep
from random import randint

jogadores = {}

print('='*40)
print(f'{"JOGO DE DADOS":^40}')
print('='*40)
for c in range(1, 5):
    nome = str(input(f'Nome do {c}º jogador: '))
    jogadores[nome] = randint(1, 6)
    print('Jogando...', end='')
    sleep(.4)
    for c in range(1, 7):
        print(f'{c}', end=' ')
        sleep(0.4)
    print()
    sleep(1)
    print(f'{nome} tirou {jogadores[nome]}')
    print('-'*40)
    sleep(1)

print('='*40)
print(f'{"COLOCAÇÃO DA RODADA:":^40}')
print('='*40)

cont = 1
for c in range(1):
    for item in sorted(jogadores, reverse=True, key=jogadores.get):
        sleep(1)
        print(f'Em {cont}º lugar - {item} com {jogadores[item]}')
        cont += 1'''

# ================ ANÁLISE DO CÓDIGO ====================================================================

# ================ MODELO CURSO EM VIDEO ================================================================


