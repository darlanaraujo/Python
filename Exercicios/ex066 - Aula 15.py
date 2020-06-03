'''
DESAFIO 066

Crie um programa que leia VÁRIOS NÚMEROS inteiros. O programa só vai parar quando
o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA.
No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles.

Desconsiderando o Flag
'''

soma = cont = 0

while True:
    n1 = int(input(f'Digite o {cont +1}º número: '))
    if n1 == 999:
        break
    soma += n1
    cont += 1

print(f'Você digitou {cont} números')
print(f'A soma entre eles foi: {soma}')