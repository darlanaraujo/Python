'''
DESAFIO 086

Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e preencha com valores
lidos pelo teclado.

[ 0 ][ 1 ][ 2 ]
[ 3 ][ 4 ][ 5 ]
[ 6 ][ 7 ][ 8 ]

No final, mostre a MATRIZ na tela, com a formatação correta
'''
# =============== MODELO CRIADO =======================================================================================
linha = []

for c in range(0, 9):
    linha.append(int(input(f'Digite o {c +1}º valor: ')))

print('='*30)
print(f'[{linha[0]:^5}][{linha[1]:^5}][{linha[2]:^5}]')
print(f'[{linha[3]:^5}][{linha[4]:^5}][{linha[5]:^5}]')
print(f'[{linha[6]:^5}][{linha[7]:^5}][{linha[8]:^5}]')

# ================= ANÁLISE DO CÓDIGO =================================================================================
'''
Acredito que meu código seja mais simples de entender, uma vez que faço a divisão dos valores no print. Já que a tabela
é pre-definida com 9 valores, não vejo por que ficar fazendo laços se posso juntar todos os valores dentro da lista e
separalos por posição no print.
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))

print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''

# OBSERVAÇÃO;
'''Levei um tempo para entender que o primeiro FOR definica a quantidade de listas dentro da lista, já o segundo
define a quantidade de informações dentro de cada lista.'''