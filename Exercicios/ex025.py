#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

print('{:=^40}'.format('EXERCICIO 25'))
nome=str(input('Digite um nome qualquer: ')).strip()
print('O nome digitado contem Silva: {}'.format('silva' in nome.lower()))
print('{:=^40}'.format('='))