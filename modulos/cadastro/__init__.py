# ============== CÓDIGO BASE =====================================================================================
from time import sleep

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
    elif resp == 'B':
        consulta()
    elif resp == 'C':
        excluir()
    elif resp == 'D':
        exit()
    else:
        sleep(.5)
        print('| \033[31mERRO! Escolha uma das opções válidas!\033[m')
        sleep(.5)
        return inicio()


def cabecalho(msg):
    print('|', '='*50, '|')
    print(f'|{msg.center(50)}  |')
    print('|', '='*50, '|')
    sleep(.5)


def validacao(msg):
    print(f'| {msg}', end='')
    for c in range(1, 5):
        sleep(.5)
        print('.', end='')
    print('Concluido.')
    return inicio()


def cadastro():
    cabecalho('CADASTRO')
    nome = str(input('| Nome completo: ')).strip().upper()
    sleep(.5)
    validacao('Adicionando')


def consulta():
    print('| Ainda em construção')


def excluir():
    print('| Ainda em construção')


def exit():
    print('| Finalizando', end='')
    sleep(.5)
    for c in range(1, 5):
        print('.', end='')
        sleep(.5)
    print('Volte sempre!')

def inicio():
    cabecalho('SISTEMA DE CADASTRO')
    sleep(.5)
    menu()


# ============== CÓDIGO MELHORADO =====================================================================================

# ============== ANÁLISE DO CÓDIGO ====================================================================================

# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
