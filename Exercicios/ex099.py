'''
DESAFIO 099

Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS
com valores inteiros.

Seu programa tem que ANALISAR todos os VALORES e dizer qual deles É O MAIOR.
'''
# ================= MODELO CRIADO =====================================================================================
from time import sleep
num = []
def maior(* num):
    print('Analisando os valores: ', end='')
    for valor in num:
        print(valor, end=' ')
        sleep(.5)
    print()
    print(f'{len(num)} números foram informado. O maior valor é {max(num)}')

while True:
    num.append(int(input('Digite um valor: ')))
    print('='*40)
    resp = str(input('Deseja adicionar outro? [S/N]: '))
    if resp in 'nN':
        break
print('='*40)
maior(* num)
# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
