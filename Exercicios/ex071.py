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



cliente1 = clinete2  = cliente3 = cliente4 = cliente5 = ''

saldo = randint(0, 10000)
saldo = saldo

# ============== DEFINIÇÃO DO LAÇO PARA O MENU ===============================================

def menu():
    while True:
        print(f'|{"$" * 70}|')
        print(f'|{"$" * 70}|')
        print(f'|\033[33m{"ÁREA DO CLIENTE: " + nome:^70}\033[30m|')
        print(f'|{"-" * 70}|')
        print(f'|{" [1] CONSULTAR SALDO EM CONTA:":<70}|')
        print(f'|{" [2] SACAR VALOR DA CONTA:":<70}|')
        print(f'|{"":^70}|')
        resp = str(input(f'| ESCOLHA A OPÇÃO DESEJADA: ')).upper().strip()[0]
        print(f'|{"-" * 70}|')

        if resp == '1' or resp == 'C':
            print(f'| SEU SALDO EM CONTA É R$ \033[33m{saldo}\033[30m reais')
            return retur()

        if resp == '2' or resp == 'S':
            return soma(saldo)

        else:
            print(f'| \033[31m{"OPÇÃO INVÁLIDA! DIGITE CORRETAMENTE":^70}\033[30m')
            break

# ============== DEFINIÇÃO DO LAÇO PARA CALCULO DE CEDULAS ===================================

def soma(saldo):
    tot50 = tot20 = tot10 = tot2 = total = 0
    while True:
        valor = int(input(f'| QUAL VALOR DESEJA SACAR R$ '))
        total = valor
        saldo -= valor
        print(f'|{"-" * 70}|')

        if valor <= saldo:
            while True:
                if valor >= 50:
                    tot50 += 1
                    valor -= 50

                elif valor < 50 and valor >= 20:
                    tot20 += 1
                    valor -= 20

                elif valor < 20 and valor >= 10:
                    tot10 += 1
                    valor -= 10

                elif valor < 10 and valor >= 2:
                    tot2 += 1
                    valor -= 2
                else:
                    return conclusao(tot50, tot20, tot10, tot2, total, saldo)
        else:
            print(f'|{"VALOR NÃO DISPONIVEL EM CONTA":^70}|')
            return menu()

# ============== DEFINIÇÃO PARA RETORNO DO MENU ==============================================

def retur():
    while True:
        retur = str(input('| RETORNAR AO MENU PRINCIPAL? [S/N]: ')).upper().strip()[0]
        print(f'|{"-" * 70}|')
        if retur == 'S':
            return menu()

        elif retur == 'N':
            break

        else:
            print(f'| \033[31m{"OPÇÃO INVÁLIDA! DIGITE CORRETAMENTE":^70}\033[30m')


# ============== INÍCIO DO PROGRAMA - CABEÇALHO ==============================================
def cabecalho():
    print(f'\033[30m|{"-"*70}|')
    print(f'|{"$"*70}|')
    print(f'|{"$"*70}|')
    print(f'|\033[33m{"CAIXA ELETRÔNICO 24H":^70}\033[30m|')
    print(f'|{"$"*70}|')
    print(f'|{"$"*70}|')
    print(f'|\033[32m{"NOTAS: R$ 2,00 R$ 10,00 R$ 20,00 R$ 50,00 REAIS":^70}\033[30m|')
    print(f'|{"-"*70}|')

# ============= DEFINIÇÃO DA CONCLUSÃO =====================================================================

def conclusao(tot50, tot20, tot10, tot2, total, saldo):
    if tot50 >= 1:
        print(f'| TOTAL DE {tot50} CEDULAS DE R$ 50,00 REAIS')
    if tot20 >= 1:
        print(f'| TOTAL DE {tot20} CEDULAS DE R$ 20,00 REAIS')
    if tot10 >= 1:
        print(f'| TOTAL DE {tot10} CEDULAS DE R$ 10,00 REAIS')
    if tot2 >= 1:
        print(f'| TOTAL DE {tot2} CEDULAS DE R$ 2,00 REAIS')
    print(f'|{"-"*70}|')
    print(f'| VALOR TOTAL SACADO R$ {total} REAIS')
    print(f'|{"-" * 70}|')
    print(f'| SALDO RESTANTE R$ {saldo} REAIS')

    return retur()

# ============= ÁREA DO CLIENTE =============================================================================
cabecalho()
nome = str(input('| NOME DO CLIENTE: ')).upper().strip()
menu()