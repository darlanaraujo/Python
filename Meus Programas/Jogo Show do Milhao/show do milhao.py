# ===================== IMPORTAÇÕES ===================================================================================
from time import sleep
from random import randint
from pygame import mixer

# ===================== VARIAVEIS GLOBAIS =============================================================================
c = ('\033[m'     # 0 = Sem cor
       '\033[30m'   # 1 = Branco
       '\033[31m'   # 2 = Vermelho
       '\033[32m'   # 3 = Verde
       '\033[33m'   # 4 = Amarelo
       '\033[34m'   # 5 = Azul
       '\033[35m'   # 6 = Roxo
       )

sc = '\033[m'  # 0 = Sem cor
br = '\033[30m'  # 1 = Branco
vm = '\033[31m'  # 2 = Vermelho
vd = '\033[32m'  # 3 = Verde
am = '\033[33m'  # 4 = Amarelo
az = '\033[34m'  # 5 = Azul
rx = '\033[35m'  # 6 = Roxo
# ===================== FUNÇÕES DO JOGO ===============================================================================
def inicio():
    layout()
    sleep(2)
    menu()


def cadastro():
    cabecalho('CADASTRO DO JOGADOR')
    nome = str(input('Nome do jogador: ')).title().strip()
    linha()
    print(f'{"Seja bem vindo(a) "f"{am}{nome}{br} começa agora o jogo "f"{am}SHOW DO MILHÃO!{br}"}')
    linha()
    while True:
        resp = str(input('VAMOS JOGAR? [S/N]: ')).upper().strip()[0]
        linha()
        if resp == 'S':
            print('Começo') # aqui vai para pergunta!
        elif resp == 'N':
            cabecalho('MENU DO JOGO')
            menu()
            break
        else:
            erro('ERRO! Dados inválidos. Digite corretamente!')


def menu():
    print(f'{am}A) {br}COMEÇAR NOVO JOGO')
    print(f'{am}B) {br}RANKING DOS JOGADORES')
    print(f'{am}C) {br}MANUAL DO JOGO')
    print(f'{am}D) {br}SAIR DO JOGO')
    linha()
    while True:
        resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).strip().upper()[0]
        if resp == 'A':
            cadastro()
        elif resp == 'B':
            print('Placar do jogo') #placar(arq)
        elif resp == 'C':
            print('Regras do jogo') #regras()
        elif resp == 'D':
            linha()
            print('Saindo do jogo', end='')
            sleep(.5)
            for c in range(1, 6):
                print('.', end='')
                sleep(.5)
            sleep(.5)
            print('Até a próxima!')
            break
        else:
            erro('ERRO! Dados inválidos!')


# ===================== FUNÇÕES DO SISTEMA ============================================================================
def layout():
    som('audio/abertura.mp3')
    print(br)
    linha('=')
    print(f'|{am+"JOGO SHOW DO MILHÃO - V1.0".center(78)+br}|')
    linha('=')
    print(f'|{am+"BEM VINDO AO JOGO SHOW DO MILHÃO!".center(78)+br}|')
    linha('=')
    print(f'|{az+"Acerte as perguntas e concorra ao premio de R$ 1.000,000,00 de reais".center(78) + br}|')
    linha('=')


def cabecalho(msg):
    print(br)
    linha()
    print(f'|{am}{msg.center(78)}{br}|')
    linha()


def som(audio):
    mixer.init()
    mixer.music.load(audio)
    mixer.music.play()


def linha(caractere='=', tam=80):
    print(caractere * tam)


def erro(msg):
    linha()
    print(f'{vm}{msg}{br}')
    linha()
# ===================== INÍCIO DO PROGRAMA ============================================================================
inicio()
