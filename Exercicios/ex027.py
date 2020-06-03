'''
Faça um programa que leia o nome completo de uma pessoa,
e mostre em seguida o primeiro e o último nome separadamente.
'''

print('{:=^40}'.format('EXERCICIO 027'))
print('')
nome=str(input('Digite seu nome completo: ')).strip()
nome=nome.title().split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
print('')
print('{:=^40}'.format('='))
