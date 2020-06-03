'''
DESAFIO 088

Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa
vai perguntar QUANTOS JOGOS serão gerados e vai SORTEAR 6 NÚMEROS ENTRE 1 E 60
para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.
'''
# ================== MODELO CRIADO ====================================================================================
# Funções globais;
from random import randint
from time import sleep
palpites = []

# Início do programa;
print('='*40)
print(f'\033[33m{"JOGO DA MEGA SENA":^40}\033[m')
print('='*40)
perg = int(input('Quantos jogos deseja criar?: '))
print('-'*40)
for c in range(0, perg):
    palpites.append([randint(1, 10), randint(11, 20), randint(21, 30),
                     randint(31, 40), randint(41, 50), randint(51, 60)])

for p, c in enumerate(palpites):
    print(f'Jogo {p+1}: {c}')
    sleep(1)

print('='*40)
print(f'\033[33m{"BOA SORTE":^40}\033[m')
print('='*40)

# ================== ANÁLISE DO CÓDIGO ================================================================================
'''
Em relação a números de linha e simplicidade, meu código ficou mais limpo e fácil de ler. Tirando as 'firulas' o código
apenas 9 linhas. Mesmo tendo usado um recurso manual para sorteio dos 6 números, ainda assim prefiro meu código.
'''
# ================== MODELO CURSO EM VIDEO ============================================================================
'''from random import randint
from time import sleep

lista = list()
jogos = list()

print('-'*30)
print('     JOGA NA MEGA SENAMA     ')
print('-'*30)

quant = int(input('Quantos jogos você quer que eu sortei? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)
'''