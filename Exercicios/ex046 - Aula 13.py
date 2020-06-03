'''
DESAFIO 046

Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artificio,
indo de 10 até 0, com uma pausa de 1 segundo entre elas.

Utilize a bibliotenca time.
'''

import time

print('{}{}{}'.format('|', '=' * 100, '|'))
print('{}{:^100}{}'.format('|', 'CONTAGEM REGRESSIVA PARA O FIM DE ANO', '|'))
print('{}{}{}'.format('|', '=' * 100, '|'))

for comando in range(10, - 1,  -1):
    time.sleep(1)
    print('{}'.format(comando), end = ' ')#, time.sleep(1)
print()
time.sleep(1)
print('!!!!!!! FELIZ ANO NOVO !!!!!!')

