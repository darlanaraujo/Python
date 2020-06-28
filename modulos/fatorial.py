def fatorial(n):
    """
        --> A função recebe um número definido pelo usuário ou pelo programa, faz o calculo e retorna um valor.
    :param n: Recebe o número a ser calculado
    :return: Retorna o valor do fatorial
    """
    f = 1
    for c in range(1, n +1):
        f *= c
    return f