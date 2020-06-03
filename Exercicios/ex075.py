'''
DESAFIO 075

Desenvolva um programa que leia QUATRO VALORES pelo teclado, e GUARDE-OS
em uma TUPLA. No final mostre:

A) QUANTAS VEZES APARECEU O VALOR 9.
B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
C) QUAIS FORAM OS NÚMEROS PARES.
'''
# ================ MODELO CRIADO ============================================
'''lista1 = lista2 = lista3 = lista4 = ()
nove = tres = pos = 0
pares = []

for c in range(1, 5):
    num = int(input(f'Digite o {c}º número: '))
    if c == 1:
        lista1 = num
    if c == 2:
        lista2 = num
    if c == 3:
        lista3 = num
    if c == 4:
        lista4 = num
    if num == 9:
        nove += 1
    if num == 3:
        if tres != 3:
            tres = num
            pos = c
    if num % 2 == 0:
        pares.append(num)
print(f'O numero 9 apareceu {nove} vezes')
print(f'A primeira vez que o número 3 foi digitado foi {pos}.')
print(f'Os numeros pares digitados foram {pares}')'''

# ============== MODELO CURSO EM VIDEO ======================================

valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'Os números digitados foram: {valores}')
print(f'O número 9 foi digitado {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 foi digitado a primeira vez na posição: {valores.index(3) +1}')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os números pares foram: ', end= '')
for n in valores:
    if n % 2 == 0:
        print(f'{n}', end= ' ')