'''
DESAFIO 055

Faça um programa que LEIA O PESO de CINCO PESSOAS.
No final, mostre QUAL FOI O MAIOR E O MENOR PESO LIDO.
'''

# ================== INICIO DO PROGRAMA ===============================================

# Essa forma deu errado por fazer a base. Qualquer numero menor que a base assume o menor, mesmo que,
# em algum momento o peso tenha sido 35kg se depois digitar qualquer número menor que a base porem menor
# que o menor, ainda assim o numero maior vai assumir o menor.
'''
menor = 0
maior = 0
base = 50

for c in range(1, 6):
    peso = float(input('Informe o {}º peso: '.format(c)))
    if peso < base:
        menor = peso
    if peso > menor and peso > maior:
        maior = peso

print('O MAIOR peso informado foi {} Kg, e o MENOR peso foi {} Kg'.format(maior, menor))
'''
# ==================== OUTRA FORMA DE FAZER O PROGRAMA =========================================

menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MENOR peso informado foi {}Kg'.format(menor))
print('O MAIOR peso informado foi {}Kg'.format(maior))
