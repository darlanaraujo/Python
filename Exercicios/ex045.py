'''
DESAFIO 045

Crie um programa que faça o COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

'''

from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
sorteio = randint(0, 2)

maquina = lista[sorteio]
print('|'+'-='*15+'|')
print('| REGRAS DO JOGO:\n| \n| PAPEL VENCE PEDRA; \n| PEDRA VENCE TESOURA; \n| TESOURA VENCE PAPEL;')
print('|'+'-='*15+'|')
sleep(1)
jogador = str(input('| FAÇA A SUA JOGADA: '))
print('| JO')
sleep(1)
print('| KEN')
sleep(1)
print('| PÔ')
print('|'+'-='*15+'|')
print('| MAQUINA JOGA: {}'.format(maquina))
