'''
DESAFIO 079

Crie um programa onde o usuário possa digitar VÁRIOS VALORES Nº e
cadastre-os em uma LISTA. Caso o número já exista lá dentro, ele
NÃO SERÁ ADICIONADO.
No final, serão exibidos todos os VALORES ÚNICOS digitados, em
ORDEM CRESCENTE.
'''
# =============== MODELO CRIADO =======================================
valores = []

def loop():
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            return cadastro()
        elif resp == 'N':
            break
        else:
            print('\033[31mATENÇÃO! Informação inválida, digite corretamente.\033[m')

def cadastro():
    n1 = int(input('Digite um número: '))
    valores.count(n1)
    valores.append(n1)

    if valores.count(n1) > 1:
        print(f'\033[31mO número \033[33m{n1} \033[31mjá está na lista. \033[33mDigite outro número.\033[m')
        valores.pop()
        return cadastro()
    else:
        print(f'O número {n1} foi adicionado com sucesso!')

    return loop()

# ============ INÍCIO DO PROGRAMA
cadastro()
print(f'Lista dos números cadastrado: {sorted(valores)}')


# ============== MODELO CURSO EM VIDEO =========================================
'''numeros = []

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar...')

    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'nN':
        break
print('=-'*30)
numeros.sort()
print(f'Os números cadastrados foram {numeros}')'''