def leiadinheiro(msg):
    from modulos.utlidadesCeV import moeda
    ok = False
    valor = 0
    while True:
        n = str(input(msg))

        if ',' in n:
            n = n.replace(',', '.')
            valor = float(n)
            ok = True

        elif n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print('ERRO! Digite apenas valores númericos!')

        if ok:
            break

    return moeda.resumo(valor, 35, 22)


def dinheiro(a):
    print(f'O valor digitado foi R$ {a}')


dinheiro('1.250,12')
