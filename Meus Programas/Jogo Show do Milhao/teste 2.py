'''from random import randint

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

pulo = 3
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
import pygame

pygame.mixer.init()
pygame.mixer.music.load('audio/frase_dificil_ajuda.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass