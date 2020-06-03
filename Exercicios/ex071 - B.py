'''
DESAFIO 071

Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No início, pergunte ao usuário qual será o  VALOR A SER SACADO
(Nº Int) e o programa vai informar QUANTAS CÉDULAS de cada valor
serão entregues.

Obs. Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''
# =========== FUNÇÕES GLOBAIS DO PROGRAMA =============================

from time import sleep
from random import randint


n1 = randint(1, 10000)
# ============== DEFINIÇÃO DO CABEÇALHO ==============================================
def cabecalho(txt):
    print(f'\033[30m|{"-"*70}|')
    print(f'|{"$"*70}|')
    print(f'|{"$"*70}|')
    print(f'|\033[33m{txt:^70}\033[30m|')
    print(f'|{"$" * 70}|')
    print(f'|{"$" * 70}|')
    print(f'|\033[32m{"NOTAS: R$ 2,00 R$ 5,00 R$ 10,00 R$ 20,00 R$ 50,00 REAIS":^70}\033[30m|')
    print(f'|{"-" * 70}|')
    clientes('ÁREA DO CLIENTE: ')

# ============== DEFINIÇÃO CADASTRO DOS CLIENTES =====================================
def clientes(txt):
    cliente = list()
    cliente.append(str(input('| NOME DO CLIENTE: ')).upper().strip())

    print(f'\033[30m|{"-" * 70}|')
    print(f'|{"#" * 70}|')
    print(f'|{"#" * 70}|')
    print(f'|\033[33m{txt:^70}\033[30m|')
    print(f'|{"#" * 70}|')
    print(f'|{"#" * 70}|')
    print(f'\033[30m|{"-" * 70}|')

    '''while True:
        cliente.append(str(input('| NOME DO CLIENTE: ')).upper().strip())
        resp = str(input('Adicionar mais... ')).upper()
        if resp == 'S':
            print(cliente)
            return clientes()
        if resp == 'N':
            break'''
    menu()
# ============== DEFINIÇÃO DO MENU ===================================================
def menu():
    print(f'|{" [1] CONSULTAR SALDO:":<70}|')
    print(f'|{" [2] SACAR SALDO DA CONTA:":<70}|')
    print(f'|{" ":^70}|')

    while True:
        resp = str(input('| ESCOLHA A OPÇÃO DESEJADA: ')).upper().strip()[0]
        if resp == '1' or resp == 'C':
            return saldo()
        elif resp == '2' or resp == 'S':
            return saque(saldo)
        else:
            print(f'|\033[31m{"ATENÇÃO! OPÇÃO INVÁLIDA, DIGITE CORRETAMENTE.":^70}\033[30m|')

# ============== DEFINIÇÃO DO SAQUE OU SALDO ========================================

def saldo():
    saldo = n1
    print(f'| O SALDO DISPONIVEL EM CONTA R$ {saldo} REAIS')
    print(f'|{"-" * 70}|')
    saque(saldo)

def saque(saldo):
    tot50 = tot20 = tot10 = tot5 = tot2 = 0

    valor = int(input('| QUAL VALOR DESEJA SACA R$ '))
    total = valor
    saldo -= valor

    while True:
        if valor >= 50:
            valor -= 50
            tot50 += 1

        if valor < 50 and valor >= 20:
            valor -= 20
            tot20 += 1

        if valor < 20 and valor >= 10:
            valor -= 10
            tot10 += 1

        if valor < 10 and valor >= 5:
            valor -= 5
            tot5 += 1

        if valor < 5 and valor >= 2:
            valor -= 2
            tot2 += 1

        else:
            break
    return conclusao(tot50, tot20, tot10, tot5, tot2, total, saldo)

# ============== DEFINIÇÃO DA CONCLUSÃO ==============================================
def conclusao(tot50, tot20, tot10, tot5, tot2, total, saldo):

    if tot50 >= 1:
        print(f'| TOTAL DE {tot50} CEDULAS DE R$ 50,00 REAIS')
    if tot20 >= 1:
        print(f'| TOTAL DE {tot20} CEDULAS DE R$ 20,00 REAIS')
    if tot10 >= 1:
        print(f'| TOTAL DE {tot10} CEDULAS DE R$ 10,00 REAIS')
    if tot5 >= 1:
        print(f'| TOTAL DE {tot5} CEDULAS DE R$ 10,00 REAIS')
    if tot2 >= 1:
        print(f'| TOTAL DE {tot2} CEDULAS DE R$ 2,00 REAIS')
    print(f'|{"-"*70}|')
    print(f'| VALOR TOTAL SACADO R$ {total} REAIS')
    print(f'|{"-" * 70}|')
    print(f'| SALDO RESTANTE R$ {saldo} REAIS')

# ============== INÍCIO DO PROGRAMA ==================================================
cabecalho('BANCO ELETRÔNICO 24 HORAS')