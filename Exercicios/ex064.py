'''
DESAFIO 064

Crie um programa que LEIA VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai
PARAR quando o usuário DIGITAR O VALOR 999, que é a CONDIÇÃO DE PARADA. No final mostre
QUANTOS NÚMEROS foram DIGITADOS e QUAL FOI A SOMA entre eles.

DESCONSIDERANDO O FLAG (999).
'''

n1 = soma = contador = 0

'''n1 = 0
soma = 0
contador = 0'''

while n1 != 999:
    n1 = int(input('Digite um número: '))
    if n1 != 999:
        soma += n1
        contador += 1

print('Você digitou {} números. A soma de todos foram {}'.format(contador, soma))