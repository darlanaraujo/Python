'''
DESAFIO 096

Faça um programa que tenha uma FUNÇÃO chamada ÁREA(), que receba as dimensões de um terreno retangular
(LARGURA e COMPRIMENTO) e mostre a ÁREA DO TERRENO.
'''
# ================= MODELO CRIADO =====================================================================================
def area(a, b):
    s = a * b
    print(f'{a}mt de Largura X {b}mt de Comprimento')
    print('='*50)
    print(f'ÁREA TOTAL DO TERRENO {s}M²')


print('='*50)
print(f'{"ÁREA DO TERRENO":^50}')
print('='*50)

a = float(input('Largura do terreno: '))
b = float(input('Comprimento do terreno: '))
print('='*50)
area(a, b)
# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
