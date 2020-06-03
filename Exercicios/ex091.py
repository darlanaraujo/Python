'''
DESAFIO 091

Crie um programa onde 4 JOGADORES joguem um DADO e tenham RESULTADOS ALEATÓRIOS.
GUARDE esses RESULTADOS em um DICIONÁRIO. No final, coloque esse dicionário em
ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no DADO.
'''
# ================ MODELO CRIADO ========================================================================
from random import randint
from time import sleep

jogadores = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)
             }

print('Valores sorteados:')

for k, i in jogadores.items():
    for item in sorted(jogadores, key= jogadores.get):
        print(f'O {k} tirou: {jogadores[item]}')
    print()



#for item in sorted(jogadores, key= jogadores.get):
#    print(f' O jogador tirou {jogadores[item]}')


# ================ MELHORIA DO CÓDIGO ===================================================================

# ================ ANÁLISE DO CÓDIGO ====================================================================

# ================ MODELO CURSO EM VIDEO ================================================================
