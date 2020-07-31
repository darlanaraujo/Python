from random import randint
from time import sleep

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

'''pulo = 3
cartas = convidados = colegas = 1

nivel1 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Em que estado brasileiro nasceu a apresentadora Xuxa?   {sc}'
    f'\n{am}A) {br}RIO DE JANEIRO'
    f'\n{am}B) {br}RIO GRANDE DO SUL'
    f'\n{am}C) {br}SANTA CATARINA'
    f'\n{am}D) {br}GOIÁS',

    f'{fvm}>>>  Quando é comemorado o dia da independência do Brasil?   {sc}'
    f'\n{am}A) {br}21 DE ABRIL'
    f'\n{am}B) {br}12 DE OUTUBRO'
    f'\n{am}C) {br}7 DE SETEMBRO'
    f'\n{am}D) {br}25 DE DEZEMBRO'
],

    'resposta': ['B', 'C']}


valor = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000,
         1000000]

premio = 0

# Essa função faz com que o sorteio não se repita.
sorteio = []
while len(sorteio) != len(nivel1['pergunta']):
    r = randint(0, len(nivel1['pergunta']) - 1)
    if r not in sorteio:
        sorteio.append(r)


def placar():
    print(f'| {" AJUDAS DO JOGO >>> "} | {"PULAR: "} {pulo} | {"CARTAS: "} {cartas} | {"CONVIDADOS: "} {convidados} | {"COLEGAS: "} {colegas} |')


def teste():
    global pulo
    placar()
    pulo -= 1
    placar()


teste()
placar()'''

'''import os
clear = lambda: os.system('cls')

nome = str(input('Qual seu nome: '))
clear()
print(f'Olá {nome}, seja bem vindo!')
str(input('Presione enter para sair.'))'''

'''import pygame

pygame.mixer.init()
pygame.mixer.music.load('audio/frase_dificil_ajuda.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass'''


def ler_pergunta(arq_pergunta):
    try:
        abrir = open(arq_pergunta, 'rt')
    except:
        print(f'Houve um ERRO na abertura do aquivo!')
    else:
        cabecalho('PERGUNTAS')
        lista = []
        temp = []

        for dados in abrir:
            dado = dados.split(';')
            dado[5] = dado[5].replace('\n', '')

            temp.append(dado[0])
            temp.append(dado[1])
            temp.append(dado[2])
            temp.append(dado[3])
            temp.append(dado[4])
            temp.append(dado[5])
            lista.append(temp[:])
            temp.clear()

        sorteio = []
        while len(sorteio) != len(lista):
            r = randint(0, len(lista) - 1)
            if r not in sorteio:
                sorteio.append(r)

        pergunta = lista[sorteio[0]]
        resposta = pergunta[5]

        print(
        f'{fvm}>>>  {pergunta[0]}?   {sc}'
        f'\n{am}A) {br}{pergunta[1]}'
        f'\n{am}B) {br}{pergunta[2]}'
        f'\n{am}C) {br}{pergunta[3]}'
        f'\n{am}D) {br}{pergunta[4]}')
        linha()

        resp = str(input('Qual a resposta certa? ')).upper().strip()
        if resp == resposta:
            print('Certa Resposta!')
        else:
            print('Que pena! Você errou.')
        linha()


    #finally:
        #abrir.close()


def cabecalho(msg):
    print(br)
    linha('=')
    print(f'|{am}{msg.center(78)}{br}|')
    linha('=')


def linha(caractere='-', tam=80):
    print(caractere * tam)


def menu():
    print('A) CADASTRAR PERGUNTA:')
    print('B) LISTA PERGUNTA CADASTRADA:')

    while True:
        opcao = str(input('Escolha a opção desejada: [A/B]: ')).upper().strip()
        if opcao == 'A':
            nivel()
        elif opcao == 'B':
            global arq_pergunta
            n = str(input('Qual o nível da pergunta? [1/2/3/4]: ')).lower().strip()
            arq = f'pergunta_nivel{n}'
            ler_pergunta(arq_pergunta)


def inicio():
    menu()


def nivel():
    global arq_pergunta
    cabecalho('CADASTRO DE PERGUNTAS')
    print(f'Para cadastrar uma pergunta, defina o nivel dela entra as opções {am}1{br} - {am}2{br} - {am}3{br} ou {am}4{br}.')
    while True:
        n = str(input('Qual o nível da pergunta? [1/2/3/4]: ')).lower().strip()
        if n not in '1234':
            print(f'ERRO! Dados inválidos. Digite apenas {am}1{br} - {am}2{br} - {am}3{br} ou {am}4{br}!')
        else:
            arq_pergunta = f'pergunta_nivel{n}'
            break

    # Função para definir o nome do arquivo aonde os dados dos jogadores ficarão salvos.
    if not arquivoexiste(arq_pergunta):
        criararquivo(arq_pergunta)
    else:
        cadastro_pergunta(arq_pergunta)


def criararquivo(arq_pergunta):
    # Função que cria o arquivo (banco de dados) caso não exista.
    try:
        abrir = open(arq_pergunta, 'wt+')
        abrir.close()
    except:
        print(f'Houve um erro na criação do arquivo {arq_pergunta}')
    else:
        print(f'Arquivo {arq_pergunta} criado com sucesso!')
        cadastro_pergunta(arq_pergunta)


def arquivoexiste(arq_pergunta):
    # Função que verifica se o arquivo (banco de dados) existe.
    try:
        abrir = open(arq_pergunta, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastro_pergunta(arq_pergunta):
    while True:
        pergunta = str(input('Qual a Pergunta: ')).title().strip()
        a = str(input('Opção A: ')).upper().strip()
        b = str(input('Opção B: ')).upper().strip()
        c = str(input('Opção C: ')).upper().strip()
        d = str(input('Opção D: ')).upper().strip()
        resposta = str(input('Qual a resposta certa? [A/B/C/D]: ')).upper().strip()

        try:
            abrir = open(arq_pergunta, 'at')
        except:
            print('Houve um ERRO na abertura do arquivo!')
        else:
            try:
                abrir.write(f'{pergunta};{a};{b};{c};{d};{resposta}\n')
            except:
                print(f'ERRO ao cadastrar a pergunta')
            else:
                abrir.close()

        print('Adicionando pergunta', end='')
        for c in range(1, 6):
            print('.', end='')
            sleep(.5)
        print('concluido!')


        resp = str(input('Cadastrar outra Pergunta? [S/N]: ')).upper().strip()
        if resp == 'S':
            continue
        elif resp == 'N':
            ler_pergunta(arq_pergunta)
            break
        else:
            print('ERRO! Dados inválidos, digite apenas S ou N.')


inicio()

'''sorteio = []
while len(sorteio) != len(dado):
    r = randint(0, len(dado) -1)
    if r not in sorteio:
        sorteio.append(r)

print(sorteio)'''


