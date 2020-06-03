'''
DESAFIO 030

Crie um programa que leia um número inteiro e motre na tela se ele é
PAR ou IMPAR
'''

print('{:=^80}'.format('EXERCICIO 030'))
print()
print('{:#^161}'.format('#\n'))
print()
print('{:^80}'.format('Olá, seja bem-vindo(a) ao nosso programa!'.upper()))
print()
print('Digite um número qualquer, e vamos descobrir se ele é PAR ou IMPAR')
print()
numero = int(input('Me diga um número: '))
resto = numero % 2
print()
print(resto)
if resto == 0:
    print('Você digitou o número: {}, ele é um número PAR!'.format(numero))
else:
    print('Você digitou o número: {}, ele é um número IMPAR!'.format(numero))
print()
print('{:#^161}'.format('#\n'))
print()
print('{:=^80}'.format(' FIM DO PROGRAMA '))
