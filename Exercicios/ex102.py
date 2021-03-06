'''
DESAFIO 102

Crie um programa que tenha uma FUNÇÃO FATORIAL() que receba dois parâmetros: O Primeiro que indique o NÚMERO a calcular
e o outro chamado SHOW, que será um valor LÓGICO (OPCIONAL) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.

fatorial(n, show=False)
parâmetro n: O número a ser calculado
parâmetro show: (opcional) mostra ou não um número n
return: O valor do fatorial de um número n
'''
# ============= CÓDIGO BASE ===========================================================================================
from math import factorial

def fatorial(n1, show=False):
    '''
        --> A função recebe a informação do usuário com o nº do fatorial e a resposta com a opção se quer ou não ver
        o calculo que mostra a soma do fatorial
    :param n1: Número que define o fatorial
    :param show: Resposta do usuário se quer ou não mostrar a soma do fatorial
    :return: Mostra o resultado na tela de acordo com as escolhas do usuário.
    '''
    soma = factorial(n1)
    print('-'*60)
    print(f'O fatorial de {n1}! é: {soma}')
    print('='*60)
    if show == True:
        f = 1
        print(f'Calculando o fatorial de {n1}! ', end='')
        for c in range(n1, 0, -1):
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= n1
            n1 -= 1
        print(f)


# Pograma principal
help(fatorial)
print(fatorial(6, True))
n1 = int(input('Digite um número para ver o fatorial: '))
print('-'*60)
while True:
    resp = str(input('Deseja mostrar a toda a soma? [S/N]: ')).upper().strip()[0]
    if resp in 'N':
        fatorial(n1)
        break
    elif resp in 'S':
        fatorial(n1, show=True)
        break
    else:
        print('ERRO! Digite apenas S ou N.')
# ============= CÓDIGO MELHORADO ======================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
Os dois códigos são basicamente o mesmo. O meu código mesmo basico utilizou alguns recursos que melhora o código mesmo
deixando-o mais longo. Mas com relação a solução e resultado, estão iguais. Destaco do código do curso a chamada do
if show: que não foi necessário incluir o True uma vez que enquanto não for definido pelo usuário o parâmetro fica
apagado, então, realmente não é necessário o uso.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(5, True))