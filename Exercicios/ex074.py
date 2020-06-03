'''
DESAFIO 074

Crie um programa que vai GERAR CINCO NÚMEROS ALEATÓRIOS e colocar em uma
TUPLA.

Depois disso, mostre a LISTAGEM DOS NÚMEROS gerados e também indique o
MENOR e o MAIOR valor que ESTÃO NA TUPLA.
'''
# ======================= MODELO CRIADO =======================================================
'''from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

menor = maior = 0

print('Lista de números sorteados: ', end= '')
for pos, c in enumerate(numeros):
    print(f'{c}',end= ' - ')
    if pos == 0:
        menor = c
        maior = c
    else:
        if c > maior:
            maior = c
        elif c < menor:
            menor = c

print('Fim')
print(f'O menor número foi {menor}')
print(f'O maior número foi {maior}')'''

# ===================== MODELO CURSO EM VIDEO ===================================================
from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
#print(numeros)
print('Números sorteados: ', end= '')
for c in numeros:
    print(f'{c}', end= ' ')
print()
print(f'O maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')