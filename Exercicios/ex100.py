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
par = []

def sorteia():
    for c in range(1, 6):
        a = randint(0, 10)
        numeros.append(a)
    somapar()

def somapar():
    soma = 0
    print(f'Sorteando os {len(numeros)} números >>> ', end='')
    for p, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
            par.append(v)
        sleep(.5)
        print(f'{v}', end=' ')
    print('Fim!')
    sleep(1)
    print(f'A soma dos valores pares foi {soma}. Sendo eles {par}')

sorteia()

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================
'''
Analisando os dois código ambos são parecidos, a unica diferença fica por conta da organização do código. No meu achei
que ficou mais completo, já que uso o len para informar a quantidade de números sorteados, e ao mostrar a soma dos
números pares, eu mostro quais foram os números separados da primeira lista. Outra diferença foi não ter dado uma
atribuição a função, não foi necessário. 
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
'''from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somapar(números)'''