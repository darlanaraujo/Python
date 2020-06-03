'''
DESAFIO 060

Faça um programa que LEIA UM NÚMERO QUALQUER e mostre o seu FATORIAL.

ex: 5! = 5x4x3x2x1 = 120

Faça o programa com os dois laços, while e for.
'''

# ======================= FORMA SIMPLES USANDO FUNÇÃO DO PYTHON =====================================================

'''from math import factorial

n1 = int(input('Digite um número: '))
soma = factorial(n1)
print('O fatorial de {}! é = {}'.format(n1, soma))'''

# ======================== FORMA MANUAL DE FAZER USANDO RECURSOS MATEMATICOS ========================================

'''print('Digite um número a sua escolha para ver o seu fatorial.')
print('=-'*30)
n1= int(input('Digite um número: '))
print('-='*30)

f = 1 #Função que vai fazer a multiplicação do numero digitado

print('Calculando fatorial de {}! = '.format(n1), end= '')

# Laço que vai fazer a sequencia de numeros aparecer na tela
while n1 > 0:
    print('{}'.format(n1), end= '')
    print(' x ' if n1 > 1 else ' = ', end='')
    f *= n1
    n1 -= 1 #Essa formula faz com que a cada contagem ele multiplique por um numero a menos.
print('{}'.format(f))'''

# ======================== USANDO O LAÇO FOR ==============================================================

print('Digite um número a sua escolha para ver o seu fatorial.')
print('=-'*30)
n1 = int(input('Digite um número: '))
print('-='*30)

f = 1
print('Calculando o fatorial de {}! = '.format(n1), end= '')
for c in range(n1, -0, -1):
    print(c, end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    f *= n1
    n1 -= 1 #Essa formula faz com que a cada contagem ele multiplique por um numero a menos.
print('{}'.format(f))