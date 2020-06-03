'''
DESAFIO 051

Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
No final, mostre os 10 PRIMEIROS TERMOS dessa PROGRESSÃO.

***Exemplo: Começa no 01 até 100, pulando de 10 em 10.
'''
from time import sleep
c = 0
termo = int(input('DIGITE O PRIMEIRO TERMO: '))
razao = int(input('DIGITE A RAZÃO: '))
decimo = termo + (10 -1) * razao

for c in range(termo, decimo + razao, razao):
    print('{} '.format(c), end = '-> '), sleep(1)

print('ACABOU')