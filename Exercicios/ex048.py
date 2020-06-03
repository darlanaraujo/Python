'''
DESAFIO 048

Faça um programa que CALCULE A SOMA entre TODOS OS NÚMEROS IMPARES
que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500.
'''

soma = 0 # Contador
valor = 0 # Acumulador

for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma += c #Contador
        valor += 1 #Acumulador

print('A soma de todos os {} valores solicitados é {}'. format(valor, soma))


'''
from time import sleep

print('Segue uma lista com os números IMAPARES de 1 até 500:')
for contagem in range(0, 500+1, 3):
    resto = contagem % 2
    if resto == 1:
        sleep(1/2)
        print(contagem, end = ' ')

print('Acabou')

'''