def aumentar(n, p, form=False):
    porc = n / 100 * p
    soma = n + porc
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def diminuir(n, p, form=False):
    porc = n / 100 * p
    soma = n - porc
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def dobro(n, form=False):
    soma = n * 2
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def metade(n, form=False):
    soma = n / 2
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def moeda(n):
    n = f'R$ {n:.2f}'
    return n


def resumo(v, a, d):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'{"Preço analisado:":<22} {moeda(v)}')
    print(f'{"Dobro do preço:":<22} {moeda(dobro(v))}')
    print(f'{"Metade do preço:":<22} {moeda(metade(v))}')
    print(f'{a}{"% de aumento:":<20} {moeda(aumentar(v, a))}')
    print(f'{d}{"% de redução:":<20} {moeda(diminuir(v, d))}')
    print('-'*35)

