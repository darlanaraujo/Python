# ============== CÓDIGO BASE =====================================================================================
'''from time import sleep
from modulos.cadastro.arquivo import *

def menu():
    print('| A) CADASTRAR NOVA PESSOA')
    print('| B) CONSULTAR PESSOAS CADASTRADAS')
    print('| C) EXCLUIR PESSOA CADASTRADA')
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


def cabeçalho(msg):
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
    cabeçalho('CADASTRO')
    nome = str(input('| Nome completo: ')).strip().upper()
    sleep(.5)
    validacao('Adicionando')


def consulta():
    arq = 'cadastrodepessoas.txt'
    if not arquivoexiste(arq):
        criararquivo(arq)
        return lerarquivo(arq)
    else:
        lerarquivo(arq)


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
    cabeçalho('SISTEMA DE CADASTRO')
    sleep(.5)
    menu()'''


# ============== CÓDIGO MELHORADO =====================================================================================

# ============== ANÁLISE DO CÓDIGO ====================================================================================
'''
PARTE 1 - Nessa primeira parte os códigos mostram o mesmo resultado, mesmo tendo diferença. As diferenças ficam por
conta do menu, que no meu codigo foi criado uma função e o programa principal apenas chama o início. No código do
curso tem um while e alguns comandos no código principal.

PARTE 2 - Essa parte eu não consegui fazer, não havia nenhuma aula anterior que mostrasse como chegar ao resultado.
As funções que foram criadas para conferir se arquivo existia ou se seria necessário cria-lo está dentro do modulo
modulos/cadastro/arquivo.

PARTE 3 - Essa parte acabei nao fazendo. Optei por terminar de ver a conclusão do curso.
'''
# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue #Esse comando faz com que o programa volte para o while nesse ponto.
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc


