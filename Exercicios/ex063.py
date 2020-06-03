'''
DESAFIO 063

Faça um programa que LEIA UM NÚMERO 'N' inteiro qualquer e mostre na tela
os 'N' PRIMEIROS ELEMENTOS de um SEQUENCIA DE FIBONACCI.

EX: 0 > 1 > 1 > 2 > 3 > 5 > 8

'''

print('='*40)
print('{:^40}'.format('SEQUENCIA DE FIBONACCI'))
print('-='*20)
n1 = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
cont = 3

print('='*40)
print('{} -> {}'.format(t1, t2), end= '')

while cont <= n1:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end= '')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('='*40)