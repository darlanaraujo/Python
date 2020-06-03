'''
DESAFIO 082

Crie um programa que vai LER VÁRIOS Nº e colocar em uma LISTA.

Depois disso, CRIE DUAS LISTAS EXTRAS que vão conter apenas os
valores PARES e os IMPARES digitados.

Ao final, mostre o conteúdo das TRÊS LISTAS.
'''

# ============== MODELO CRIADO =================================================
lista = []
par = []
impar = []

def loop():
    while True:
        print('=-'*20)
        resp = str(input('Deseja cadastrar outro? [S/N]: ')).upper().strip()[0]
        print('=-' * 20)
        if resp == 'S':
            return inicio()
        if resp == 'N':
            break
        else:
            print('\033[31mDados invalidos! Digite corretamente.\033[m')
            return loop()

def inicio():
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    if n1 % 2 == 0:
        par.append(n1)
    else:
        impar.append(n1)
    loop()

# INÍCIO DO PROGRAMA;
inicio()
print(f'Lista geral dos números cadastrados: {lista}')
print(f'Lista com números pares cadastrados: {par}')
print(f'Lista com números impares cadastrados: {impar}')

# =================== MODELO CURSO EM VIDEO =======================================================================
'''num = []
pares = []
ímpares = []

while True:
    num.append(int(input('Digite um número: ')))

    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'nN':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print('=-'*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')'''