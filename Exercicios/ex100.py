'''
DESAFIO 100

Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas
SORTEIA() e SOMAPAR(). A primeira função vai sortear 5 NÚMEROS e vai colocá-los
dentro da lista e a segunda função vai mostrar a SOMA entre todos os valores
PARES sorteados pela função anterior.
'''
# ================= MODELO CRIADO =====================================================================================
from random import randint
from time import sleep
numeros = []

def sorteia():
    for c in range(1, 6):
        a = randint(0, 10)
        numeros.append(a)
    somapar()

def somapar():
    soma = 0
    print(f'Sorteando os números >>> ', end='')
    for p, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
        sleep(.5)
        print(f'{v}', end=' ')
    print('Fim!')
    sleep(1)
    print(f'A soma dos valores pares foi {soma}')

sorteia()

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
