'''
DESAFIO 098

Faça um programa que tenha uma FUNÇÃO chamada CONTADOR(), que receba três PARÂMENTROS:
INÍCIO, FIM e PASSO e realize a contagem

Seu programa tem que realizar TRÊS CONTAGENS através da função criada:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA.
'''
# ================= MODELO CRIADO =====================================================================================
'''from time import sleep
def contador(a, b, c):
    print('=' * 50)
    print(f'Contatem de {a} até {b} de {c} em {c}:')
    for c in range(a, b, c):
        print(c, end=' ')
        sleep(.5)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('='*50)
print('Contagem personalizada. Defina a sua escolha')
a = int(input('Defina o Início: '))
b = int(input('Defina o Fim: '))
c = int(input('Defina o intervalo: '))
contador(a, b, c)'''
# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================
'''
Apesar do meu código funcionar em parte, sem dúvida o código docurso ficou nuito mais completo fechando todas as pontas
que o meu código tinha com numeros negativos.
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim!')

    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('Fim!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' *20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('INÍCIO:    '))
fim = int(input('FIM:       '))
pas = int(input('PASSO:     '))
contador(ini, fim, pas)

