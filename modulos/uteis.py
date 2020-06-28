def fatorial(n):
    """
        --> A função recebe um número definido pelo usuário ou pelo programa, faz o calculo e retorna um valor.
    :param n: Recebe o número a ser calculado
    :return: Retorna o valor do fatorial
    """
    from math import factorial
    f = 1
    soma = factorial(n)
    print(f'Calculando o fatorial de {n}! ', end='')
    for c in range(n, 0, -1):
        print(c, end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
    f *= c
    
    return soma


def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
