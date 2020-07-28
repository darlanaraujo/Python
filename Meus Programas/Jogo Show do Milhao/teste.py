# ===================== IMPORTAÇÕES ===================================================================================
from time import sleep
from random import randint

import pygame

# ===================== VARIAVEIS GLOBAIS =============================================================================
# Tabela de cores;
sc = '\033[m'  # 0 = Sem cor
br = '\033[30m'  # 1 = Branco
vm = '\033[31m'  # 2 = Vermelho
vd = '\033[32m'  # 3 = Verde
am = '\033[33m'  # 4 = Amarelo
az = '\033[34m'  # 5 = Azul
rx = '\033[35m'  # 6 = Roxo
# Cores com fundo;
fvm = '\033[41;30m'  # 7 = Fundo Vermelho Letra Branca

# Ajudas do jogo;
pulo = 3
carta = 1
convidado = 1
colega = 1
# ===================== PERGUNTAS DO JOGO =============================================================================

# Formulário base para as perguntas;
f'{fvm}>>>  msg   {sc}'
f'\n{am}A) {br}msg'
f'\n{am}B) {br}msg'
f'\n{am}C) {br}msg'
f'\n{am}D) {br}msg'

nivel1 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Em que estado brasileiro nasceu a apresentadora Xuxa?   {sc}'
    f'\n{am}A) {br}RIO DE JANEIRO'
    f'\n{am}B) {br}RIO GRANDE DO SUL'
    f'\n{am}C) {br}SANTA CATARINA'
    f'\n{am}D) {br}GOIÁS',
    # Pergunta 1
    f'{fvm}>>>  Qual é o nome dado ao estado da água em forma de gelo?   {sc}'
    f'\n{am}A) {br}LÍQUIDO'
    f'\n{am}B) {br}SÓLIDO'
    f'\n{am}C) {br}GASOSO'
    f'\n{am}D) {br}VAPOROSO',
    # Pergunta 2
    f'{fvm}>>>  Qual era o apelido da cantora Elis Regina?   {sc}'
    f'\n{am}A) {br}GAUCHINHA'
    f'\n{am}B) {br}PAULISTINHA'
    f'\n{am}C) {br}PIMENTINHA'
    f'\n{am}D) {br}ANDORINHA',
    # Pergunta 3
    f'{fvm}>>>  Quem é a namorada do Mickey?   {sc}'
    f'\n{am}A) {br}MARGARIDA'
    f'\n{am}B) {br}MINNIE'
    f'\n{am}C) {br}A PEQUENA SEREIA'
    f'\n{am}D) {br}OLÍVIA PALITO',
    # Pergunta 4
    f'{fvm}>>>  Fidel Castro nasceu em que país?   {sc}'
    f'\n{am}A) {br}JAMAICA'
    f'\n{am}B) {br}CUBA'
    f'\n{am}C) {br}EL SALVADOR'
    f'\n{am}D) {br}MÉXICO',
    # Pergunta 5
    f'{fvm}>>>  Quem proclamou a república no Brasil em 1889?   {sc}'
    f'\n{am}A) {br}DUQUE DE CAXIAS'
    f'\n{am}B) {br}MARECHAL RONDON'
    f'\n{am}C) {br}DOM PEDRO II'
    f'\n{am}D) {br}MARECHAL DEODORO',
    # Pergunta 6
    f'{fvm}>>>  Quem é o patrono do exército brasileiro?   {sc}'
    f'\n{am}A) {br}MARECHAL DEODORO'
    f'\n{am}B) {br}BARÃO DE MAUÁ'
    f'\n{am}C) {br}DUQUE DE CAXIAS'
    f'\n{am}D) {br}MARQUÊS DE POMBAL',
    # Pergunta 7
    f'{fvm}>>>  Qual é o signo do zodíaco de quem nasce no dia do ano-novo?   {sc}'
    f'\n{am}A) {br}VIRGEM'
    f'\n{am}B) {br}AQUÁRIO'
    f'\n{am}C) {br}CAPRICÓRNIO'
    f'\n{am}D) {br}ÁRIES',
    # Pergunta 8
    f'{fvm}>>>  A água ferve a quantos graus centígrados?   {sc}'
    f'\n{am}A) {br}200'
    f'\n{am}B) {br}100'
    f'\n{am}C) {br}170'
    f'\n{am}D) {br}220',
    # Pergunta 9
    f'{fvm}>>>  Quando é comemorado o dia da independência do Brasil?   {sc}'
    f'\n{am}A) {br}21 DE ABRIL'
    f'\n{am}B) {br}12 DE OUTUBRO'
    f'\n{am}C) {br}7 DE SETEMBRO'
    f'\n{am}D) {br}25 DE DEZEMBRO',
],
    'resposta': ['B', 'B', 'C', 'B', 'B', 'D', 'C', 'C', 'B', 'C', ]}

pulos = {'pergunta': [
        f'{fvm}>>>  Qual personagem da turma da Mônica tem apenas cinco fios de cabelo?   {sc}'
        f'\n{am}A) {br}MÔNICA'
        f'\n{am}B) {br}CEBOLINHA'
        f'\n{am}C) {br}CASCÃO'
        f'\n{am}D) {br}MAGALI',
        
        f'{fvm}>>>  Qual cantora tinha o apelido de “Ternurinha” na época da jovem guarda?   {sc}'
        f'\n{am}A) {br}SILVINHA'
        f'\n{am}B) {br}WANDERLÉIA'
        f'\n{am}C) {br}GRETCHEN'
        f'\n{am}D) {br}MARTINHA',
        
        f'{fvm}>>>  Quantas dentições naturais tem o ser humano durante a vida?   {sc}'
        f'\n{am}A) {br}UMA'
        f'\n{am}B) {br}DUAS'
        f'\n{am}C) {br}TRÊS'
        f'\n{am}D) {br}QUATRO',
        
        f'{fvm}>>>  Quantos dias tem um ano bissexto?   {sc}'
        f'\n{am}A) {br}364'
        f'\n{am}B) {br}365'
        f'\n{am}C) {br}366'
        f'\n{am}D) {br}367',
        
        f'{fvm}>>>  Quem foi técnico da Seleção brasileira de futebol na Copa de 98?   {sc}'
        f'\n{am}A) {br}ZAGALLO'
        f'\n{am}B) {br}SCOLARI'
        f'\n{am}C) {br}LUXEMBURGO'
        f'\n{am}D) {br}CARPEGIANNI',
        
        f'{fvm}>>>  O dromedário tem quantas corcovas?   {sc}'
        f'\n{am}A) {br}UMA'
        f'\n{am}B) {br}DUAS'
        f'\n{am}C) {br}TRÊS'
        f'\n{am}D) {br}QUATRO',
],
    
    'resposta': ['B', 'B', 'B', 'C', 'A', 'A']}

# Essa função faz com que o sorteio não se repita.
sorteio = []
while len(sorteio) != len(nivel1['pergunta']):
    r = randint(0, len(nivel1['pergunta']) - 1)
    if r not in sorteio:
        sorteio.append(r)

pular = []
while len(pular) != len(pulos['pergunta']):
    r = randint(0, len(pulos['pergunta']) - 1)
    if r not in pular:
        pular.append(r)

#print(sorteio)

valor = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000,
         1000000]

premio = 0

# ===================== PERGUNTAS DO JOGO =============================================================================
def perguntas(pergunta, resposta, proxima, p):
    pergunta = pergunta
    resposta = resposta

    print(pergunta)
    linha()
    som('audio/frase_entendeu.mp3')
    som('audio/frase_opcoes.mp3')
    escolha = str(input('VOCÊ VAI RESPONDER OU PEDIR AJUDA? [R/A]: ')).upper().strip()[0]
    linha()
    if escolha == 'R':
        confirmacao(pergunta, resposta, proxima)
    elif escolha == 'A':
        menu_ajuda(pergunta, resposta, proxima, p)
    else:
        erro(f'ERRO! Dados inválidos, digite apenas {am}R{br} ou {am}A{br}.')


def pula(proxima, p):
    global pulo
    pulo -= 1
    som('audio/frase_pular.mp3')
    
    pergunta = pulos['pergunta'][pular[p]]
    resposta = pulos['resposta'][pular[p]]
    
    print(pergunta)
    linha()
    confirmacao(pergunta, resposta, proxima)
            

def cartas(pergunta, resposta, proxima):
    pergunta = pergunta
    resposta = resposta
    opcoes = ['A', 'B', 'C', 'D']

    som('audio/frase_cartas.mp3')

    excluir = randint(1, 3)
    print(f'Você tirou um {excluir} !', end=' ')
    sleep(1)
    if excluir == 1:
        print('Que pena, você ainda tem 3 opções!')
    elif excluir == 2:
        print('Boa! só resta 2 opções agora.')
    elif excluir == 3:
        print('Parabéns! Agora ficou fácil...')

    print('Desconsidere as opções:', end=' ')
    for c in range(excluir):
        for p, v in enumerate(opcoes):
            if v != resposta:
                print(f'{vm} - {v}{br}', end='')
    print('\n')

    sleep(1)
    linha()
    confirmacao(pergunta, resposta, proxima)


def confirmacao(pergunta, resposta, proxima):
    print(pergunta)
    linha()
    som('audio/frase_pergunta_certa.mp3')
    while True:
        resp = str(input('QUAL A RESPOSTA CERTA? ')).upper().strip()[0]
        linha()
        som('audio/frase_pergunta.mp3')
        resp2 = str(input('VOCÊ ESTÁ CERTO DISSO, POSSO PERGUNTAR? [S/N]: ')).upper().strip()[0]
        linha()
        if resp2 == 'S':
            if resp == resposta:
                som('audio/frase_parabens.mp3')
                print('CERTA RESPOSTA!')
                som('audio/frase_acerto.mp3')
                parar()
                proxima()
            else:
                som('audio/frase_erro.mp3')
                print('QUE PENA, VOCÊ ERROU!')
                sair()
                break
        elif resp2 == 'N':
            continue
        else:
            erro(f'ERRO! dados inválidos, digite apenas {am}S{br} ou {am}N{br}.')


def menu_ajuda(pergunta, resposta, proxima, p):
    som('audio/frase_ajuda1.mp3')
    print('A) PULAR')
    print('B) CARTAS')
    print('C) CONVIDADOS')
    print('D) COLEGAS')
    linha()
    som('audio/frase_ajuda2.mp3')
    resp = str(input('E PARA QUEM VOCÊ VAI PEDIR AJUDA? ')).upper().strip()[0]
    linha()
    if resp == 'A':
        pula(proxima, p)
    elif resp == 'B':
        cartas(pergunta, resposta, proxima)


def rodada1():
    p = 0
    pergunta = nivel1['pergunta'][sorteio[0]]
    resposta = nivel1['resposta'][sorteio[0]]
    cabecalho(f' 1ª PERGUNTA, VALENDO {valor[0]} REAIS')
    placar()
    som('audio/frase_1mil.mp3')
    perguntas(pergunta, resposta, rodada2, p)


def rodada2():
    p = 1
    pergunta = nivel1['pergunta'][sorteio[1]]
    resposta = nivel1['resposta'][sorteio[1]]
    cabecalho(f' 2ª PERGUNTA, VALENDO {valor[1]} REAIS')
    placar()
    som('audio/frase_2mil.mp3')
    perguntas(pergunta, resposta, rodada3, p)
    

def rodada3():
    p = 2
    pergunta = nivel1['pergunta'][sorteio[2]]
    resposta = nivel1['resposta'][sorteio[2]]
    cabecalho(f' 3ª PERGUNTA, VALENDO {valor[2]} REAIS')
    placar()
    som('audio/frase_3mil.mp3')
    perguntas(pergunta, resposta, rodada4, p)


def rodada4():
    p = 3
    pergunta = nivel1['pergunta'][sorteio[3]]
    resposta = nivel1['resposta'][sorteio[3]]
    cabecalho(f' 4ª PERGUNTA, VALENDO {valor[3]} REAIS')
    placar()
    som('audio/frase_4mil.mp3')
    perguntas(pergunta, resposta, rodada5, p)


def rodada5():
    p = 4
    pergunta = nivel1['pergunta'][sorteio[4]]
    resposta = nivel1['resposta'][sorteio[4]]
    cabecalho(f' 5ª PERGUNTA, VALENDO {valor[4]} REAIS')
    placar()
    som('audio/frase_5mil.mp3')
    perguntas(pergunta, resposta, rodada1, p)
    
    
# ===================== FUNÇÕES DO JOGO ===============================================================================
def inicio():
    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura.mp3')
    pygame.mixer.music.play()
    layout()
    sleep(5)
    menu()


def cadastro():
    som('audio/frase_participante.mp3')
    cabecalho('CADASTRO DO JOGADOR')
    nome = str(input('Nome do jogador: ')).title().strip()
    linha()
    print(f'{"Seja bem vindo(a) "f"{am}{nome}{br} começa agora o jogo "f"{am}SHOW DO MILHÃO!{br}"}')
    linha()
    while True:
        som('audio/frase_inicio.mp3')
        resp = str(input('VAMOS JOGAR? [S/N]: ')).upper().strip()[0]
        linha()
        if resp == 'S':
            rodada1()
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
            print('Placar do jogo')  # placar(arq)
        elif resp == 'C':
            print('Regras do jogo')  # regras()
        elif resp == 'D':
            sair()
            break
        else:
            erro('ERRO! Dados inválidos!')


def sair():
    som('audio/frase_tchau.mp3')
    linha()
    print('Saindo do jogo', end='')
    sleep(.5)
    for c in range(1, 6):
        print('.', end='')
        sleep(.5)
    sleep(.5)
    print('Até a próxima!')


def parar():
    linha()
    resp = str(input('VOCÊ QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    linha()
    if resp == 'N':
        som('audio/frase_parar.mp3')
        resp2 = str(input('ESTÁ CERTO DISSO? [S/N]: ')).upper().strip()[0]
        linha()
        if resp2 == 'S':
            sair()


# ===================== FUNÇÕES DO SISTEMA ============================================================================
def layout():
    print(br)
    linha('=')
    print(f'|{am + "JOGO SHOW DO MILHÃO - V1.0".center(78) + br}|')
    linha('=')
    print(f'|{am + "BEM VINDO AO JOGO SHOW DO MILHÃO!".center(78) + br}|')
    linha('=')
    print(f'|{az + "Acerte as perguntas e concorra ao premio de R$ 1.000,000,00 de reais".center(78) + br}|')
    linha('=')
    placar()


def placar():
    print(
        f'| {am}{" AJUDAS DO JOGO >>> "}{br} | {"PULAR: "} {am}{pulo}{br} | {"CARTAS: "} {am}{carta}{br} | {"CONVIDADOS: "} {am}{convidado}{br} | {"COLEGAS: "} {am}{colega}{br} |')
    linha('=')


def cabecalho(msg):
    print(br)
    linha('=')
    print(f'|{am}{msg.center(78)}{br}|')
    linha('=')


def som(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass


def linha(caractere='-', tam=80):
    print(caractere * tam)


def erro(msg):
    linha()
    print(f'{vm}{msg}{br}')
    linha()


# ===================== INÍCIO DO PROGRAMA ============================================================================
#inicio()

resposta = nivel1['resposta'][sorteio[0]]
opcoes = ['A', 'B', 'C', 'D']
excluir = randint(1, 3)

print(f'númeo de cartas excluida: {excluir}')
print(f'Resposta certa: {resposta}')

print(f'Você tirou um {excluir} !', end=' ')
if excluir == 1:
    print('Que pena, você ainda tem 3 opções!')
elif excluir == 2:
    print('Boa! só resta 2 opções agora.')
elif excluir == 3:
    print('Parabéns! Agora ficou fácil...')

print('Desconsidere as opções:', end=' ')

lista = []

for p, v in enumerate(opcoes):
    if resposta != v:
        lista.append(v)

print(lista[-3: -0 +excluir])



'''for p, v in enumerate(opcoes):
    if resposta != v:
        print(f'{vm} - {v}{br}', end='')
    else:
        break'''

'''for p, v in enumerate(opcoes):
    for c in range(1):
        print(f'Volta número {p}')'''