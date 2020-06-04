lista = ['']


while True:
    produto = str(input('Nome do produto: ')).title().strip()
    #tratamento = produto
    lista += lista.append(produto)

    while True:
        resp = str(input('Cadastrar mais produtos? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            break
        if resp == 'N':
            break
    if resp == 'N':
        break
print(len(lista))
print(lista)
for c in lista:
    print(f'Nome do produto: {c}')

