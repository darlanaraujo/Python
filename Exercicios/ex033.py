'''
DESAFIO 033

Faça um programa que leia 3 números
e mostre qual é o MAIOR e qual é o MENOR.
'''

print('{:=^80}'.format(' EXERCICIO 033 '))
print()
print('Me diga 3 números a sua escolha, e vou te dizer qual é o MAIOR e qual o MENOR entre eles.'.upper())
print()
n1=int(input('Qual o primeiro número? '.upper()))
print()
n2=int(input('QUAL O SEGUNDO NÚMERO? '))
print()
n3=int(input('POR FIM, QUAL O ÚLTIMO NÚMERO? '))
if n1 > n2 > n3:
    print('O MAIOR NÚMERO É: {}'.format(n1))
    if n2 > n3:
        print('O MENOR NÚMERO É: {}'.format(n3))
    else:
        print('O MENOR NÚMERO É: {]'.format(n2))
elif n1 < n2 > n3:
    print('O MAIOR NÚMERO É: {}'.format(n2))
    if n1 > n3:
        print('O MENOR NÚMERO É: {}'.format(n3))
    else:
        print('O MENOR NÚMEOR É: {}'.format(n1))
else:
    print('O MAIOR NÚMERO É: {}'.format(n3))
    if n1 > n2:
        print('O MENOR NÚMERO É: {}'.format(n2))
    else:
        print('O MENOR NÚMERO É: {}'.format(n1))
print()
print('{:=^80}'.format(' FIM DO PROGRAMA '))