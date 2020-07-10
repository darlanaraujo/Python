'''
DESAFIO 115

Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar pessoas pelo seu NOME e IDADE em um arquivo de texto
simples.

O sistema só vai ter 2 OPÇÕES: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas.
'''
# ============== CÓDIGO BASE ==========================================================================================
def menu():
    print('| A) CADASTRAR')
    print('| B) CONSULTAR')
    print('| C) EXCLUIR')
    print('| D) SAIR DO PROGRAMA')
    print('|', '-'*50, '|')
    resp = str(input('| ESCOLHA A OPÇÃO DESEJADA: ')).upper().strip()[0]
    print('|', '-'*50, '|')
    if resp == 'A':
        cadastro()
    if resp == 'B':
        print('| Consultar')
    if resp == 'C':
        print('| Excluir')
    if resp == 'D':
        validacao('Finalizando')


def cabecalho(msg):
    print('|', '='*50, '|')
    print(f'|{msg.center(50)}  |')
    print('|', '='*50, '|')
    menu()


def validacao(msg):
    from time import sleep
    print(f'| {msg}', end='')
    for c in range(1, 5):
        sleep(.5)
        print('.', end='')
    print('Concluido.')


def cadastro():
    nome = str(input('| Nome completo: ')).strip().upper()
    validacao('Adicionando')


cabecalho('SISTEMA DE CADASTRO')
# ============== CÓDIGO MELHORADO =====================================================================================

# ============== ANÁLISE DO CÓDIGO ====================================================================================

# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
