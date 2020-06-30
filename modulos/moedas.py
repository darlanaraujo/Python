def aumentar(n):
    porc = n / 10
    soma = n + porc
    return soma


def diminuir(n):
    porc = n / 10 * 2.5
    soma = n - porc
    return soma


def dobro(n):
    soma = n * 2
    return soma


def metade(n):
    soma = n / 2
    return soma


def moeda(n):
    n = f'{n:.2f}'
