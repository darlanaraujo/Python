'''
DESAFIO 052

Faça um programa que leia um NÚMERO INTEIRO e
DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

***Número primo são aqueles que são divisiveis por 1 e por ele mesmo.
'''

numero = int(input('DIGITE UM NÚMERO: '))
total = 0

for c in range(1, numero +1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print()
print('\033[mO NÚMERO \033[33m{} \033[mFOI DIVISIVEL \033[33m{}\033[m VEZES'.format(numero, total))
if total == 2:
    print('POR ISSO ELE É UM NÚMERO PRIMO.')
else:
    print('POR ISSO ELE NÃO É UM NÚMERO PRIMO.')