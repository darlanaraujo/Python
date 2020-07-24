# ===================== IMPORTAÇÕES ===================================================================================
from time import sleep
from random import randint
from pygame import mixer

# ===================== VARIAVEIS GLOBAIS =============================================================================


# ===================== FUNÇÕES DO JOGO ===============================================================================
def inicio():
    layout()
    sleep(2)
    while True:
        resp = str(input('VAMOS JOGAR? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            print('Cadastro')
        elif resp == 'N':
            print('Final do jogo!')
            break
        else:
            erro('ERRO! Dados inválidos. Digite corretamente!')

# ===================== FUNÇÕES DO SISTEMA ============================================================================
def layout():
    som('audio/abertura.mp3')
    linha('=')
    print(f'|{"JOGO SHOW DO MILHÃO - V1.0".center(78)}|')
    linha('=')
    print(f'|{"BEM VINDO AO JOGO SHOW DO MILHÃO!".center(78)}|')
    linha('=')
    print(f'|{"Acerte as perguntas e concorra ao premio de R$ 1.000,000,00 de reais".center(78)}|')
    linha('=')


def som(audio):
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()


def linha(caractere='-', tam=80):
    print(caractere * tam)


def erro(msg):
    linha()
    print(f'\033[31m{msg}\033[m')
    linha()
# ===================== INÍCIO DO PROGRAMA ============================================================================
inicio()
