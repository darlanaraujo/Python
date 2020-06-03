'''
DESAFIO 050

Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a
SOMA APENAS daqueles que forem PARES. Se o valor digitado for
IMPAR, DESCONSIDERE-0.
'''

# ========================= VARIÁVEIS GLOBAIS =========================================================================

soma        = 0
pares       = 0
impar       = 0
soma2       = 0

# ========================= LAÇO DE REPETIÇÃO DE UM COMANDO ===========================================================

#Tudo que está dentro do laço vai ser repetido pelo numero de vezes que está dentro de range.
for c in range(1, 6+1):
    numero = (int(input('DIGITE {}º NÚMERO: '.format(c)))) #Dentro do formate coloquei para ler a contagem.
    if numero % 2 == 0:
        soma += numero #Seria o mesmo que soma = numero
        pares += 1

    if numero % 2 == 1:
        soma2 += numero
        impar += 1

# ========================= RESULTADO DO PROGRAMA =====================================================================

print('''VOCÊ INFORMOU {} NÚMEROS NO TOTAL.

SENDO {} NÚMEROS PARES, A SOMA DELES SÃO: {}
E {} NÚMEROS IMAPARES, A SOMA DELES SÃO: {}'''.format(c,pares, soma, impar, soma2))

