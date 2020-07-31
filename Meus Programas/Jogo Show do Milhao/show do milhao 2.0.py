# -*- encoding: utf-8 -*-
# ====================== DOCUMENTAÇÃO DO JOGO =========================================================================
'''
DESCRIÇÃO DO JOGO:
'''
# ====================== VARIAVEL GLOBAL ==============================================================================
# Importações;
from time import sleep
from random import randint
import pygame

# Tabela de cores;
sc = '\033[m'       # Sem cor
br = '\033[30m'     # Branco
vm = '\033[31m'     # Vermelho
vd = '\033[32m'     # Verde
am = '\033[33m'     # Amarelo
az = '\033[34m'     # Azul
rx = '\033[35m'     # Roxo
# Cores com fundo;
fvm = '\033[41;30m' # Fundo Vermelho Letra Branca

# Nome do arquivo para salvar dados do jogo;
arq_jogo = 'arquivo_jogo.txt'
nome = 'Jogador 1'

# Definição dos valores para cada rodada;
valor = ['R$ 1.000,00', 'R$ 2.000,00', 'R$ 3.000,00', 'R$ 4.000,00', 'R$ 5.000,00',
         'R$ 10.000,00', 'R$ 20.000,00', 'R$ 30.000,00', 'R$ 40.000,00', 'R$ 50.000,00',
         'R$ 100.000,00', 'R$ 200.000,00', 'R$ 300.000,00', 'R$ 400.000,00', 'R$ 500.000,00',
         'R$ 1.000.000,00']

# Definição para a variável de premio que será exibida ao termino da jogada e mostrá-ra o valor ganho pelo jogador.
premio = 0
acerto = 0
errar = 0
parar = 0

# Ajudas do jogo;
pulo = 3
carta = 1
convidado = 1
colega = 1
# ====================== LAYOUT DO JOGO ===============================================================================
def cabecalho(msg):
    linha(f'{br}=')
    print(f'|{am}{msg.center(78)}{br}|')
    linha('=')


def linha(caractere='-', tam=80):
    print(caractere * tam)


def placar():
    print(f'| {am}{" AJUDAS DO JOGO >>> "}{br} | {"PULAR: "} {am}{pulo}{br} | {"CARTAS: "} {am}{carta}{br} |'
          f' {"CONVIDADOS: "} {am}{convidado}{br} | {"COLEGAS: "} {am}{colega}{br} |')
    linha('=')
    print(f'| {am}{"PLACAR >>>"}{br} | {"ERRAR:"} {vm}{errar:<11.2f}{br} |'
          f' {"PARAR:"} {rx}{parar:<12.2f}{br} | {"ACERTO:"} {am}{acerto:<12.2f}{br} |')



# ====================== FUNÇÕES DO JOGO ==============================================================================
def inicio(arq):
    # Função para definir o nome do arquivo aonde os dados dos jogadores ficarão salvos.
    if not arquivoexiste(arq):
        criararquivo(arq)
    else:
        pygame.mixer.init()
        pygame.mixer.music.load('audio/abertura.mp3')
        pygame.mixer.music.play()

        cabecalho('JOGO SHOW DO MILHÃO - V2.0')
        cabecalho(f'      {am}BEM VINDO AO JOGO {br}SHOW DO MILHÃO - {am}DESENVOLVIDO POR {br}DARLAN ARAUJO       ')
        cabecalho(f'     {az}Acerte as perguntas e concorra ao premio de {vm}{valor[15]}{az} de reais{br}     ')
        sleep(5)
        menu()


def menu():
    print(f'{am}A) {br}NOVO JOGO')
    print(f'{am}B) {br}RANKING DOS JOGADORES')
    print(f'{am}C) {br}CADASTRAR PERGUNTA')
    print(f'{am}D) {br}SAIR DO JOGO')
    linha()
    while True:
        resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).strip().upper()[0]
        if resp == 'A':
            print('cadastro...')#cadastro()
        elif resp == 'B':
            som('audio/frase_lombardi.mp3')
            print('Ranking...')#ranking(arq)
        elif resp == 'C':
            #som('audio/frase_lombardi.mp3')
            print('Cadastrar perguntas...')
        elif resp == 'D':
            print('Sair do jogo...')#sair()
            break
        else:
            erro('ERRO! Dados inválidos, digite as opções do menu!')


def som(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass


def erro(msg):
    linha()
    print(f'{vm}{msg}{br}')
    linha()

# ====================== FUNÇÕES DO SISTEMA ===========================================================================
def criararquivo(arq):
    """
    Essa função cria o arquivo txt, para guardar os dados do jogo
    :param arq: Recebe o nome que será dado ao arquivo txt
    :return: Se estiver tudo correto o arquivo é criado, caso contrário uma msg de erro é gerada.
    """
    try:
        abrir = open(arq, 'wt+')
        abrir.close()
    except:
        print(f'Houve um erro na criação do arquivo {arq}')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def arquivoexiste(arq):
    """
    Essa função verifica se em algum momento o arquivo do parâmetro já foi criado.
    :param arq: Recebe o nome que será dado ao arquivo txt.
    :return: Ao tentar abrir o arquivo se estiver tudo ok o programa continua, caso contrário ele retorna uma msg erro.
    """
    try:
        abrir = open(arq, 'rt')
    except FileNotFoundError:
        erro(f'ERRO! Não foi possível abrir o arquivo {arq}')
        return False
    else:
        abrir.close()
        return True

# ====================== PROGRAMA PRINCIPAL ===========================================================================
inicio(arq_jogo)