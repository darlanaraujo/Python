# ===================== IMPORTAÇÕES ===================================================================================
from time import sleep
from random import randint
#import random
#from pygame import mixer, event
import pygame

# ===================== VARIAVEIS GLOBAIS =============================================================================
# Tabela de cores;
sc = '\033[m'       # 0 = Sem cor
br = '\033[30m'     # 1 = Branco
vm = '\033[31m'     # 2 = Vermelho
vd = '\033[32m'     # 3 = Verde
am = '\033[33m'     # 4 = Amarelo
az = '\033[34m'     # 5 = Azul
rx = '\033[35m'     # 6 = Roxo
# Cores com fundo;
fvm = '\033[41;30m' # 7 = Fundo Vermelho Letra Branca

# Ajudas do jogo;
pulo = 3
cartas = 1
convidados = 1
colegas = 1

# Definição dos valores para cada rodada;
valor = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000, 1000000]

# Definição para a variável de premio que será exibida ao termino da jogada e mostrá-ra o valor ganho pelo jogador.
premio = 0
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
    'resposta':['B', 'B', 'C', 'B', 'B', 'D', 'C', 'C', 'B', 'C',]
}

nivel2 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Quantos jogadores um jogo de vôlei reúne na quadra?   {sc}'
    f'\n{am}A) {br}SEIS'
    f'\n{am}B) {br}OITO'
    f'\n{am}C) {br}DEZ'
    f'\n{am}D) {br}DOZE',
    # Pergunta 1
    f'{fvm}>>>  Que imperador pôs fogo em Roma?   {sc}'
    f'\n{am}A) {br}TRAJANO'
    f'\n{am}B) {br}NERO'
    f'\n{am}C) {br}BRUTOS'
    f'\n{am}D) {br}CALÍGULA',
    # Pergunta 2
    f'{fvm}>>>  Como é chamado quem nasce em Milão, na Itália?   {sc}'
    f'\n{am}A) {br}MILANENSE'
    f'\n{am}B) {br}MILANOSO'
    f'\n{am}C) {br}MILISTA'
    f'\n{am}D) {br}MILANÊS',
    # Pergunta 3
    f'{fvm}>>>  O que é um oboé?   {sc}'
    f'\n{am}A) {br}VULCÃO'
    f'\n{am}B) {br}COMIDA'
    f'\n{am}C) {br}INSTRUMENTO MUSICAL'
    f'\n{am}D) {br}TRIBO INDÍGENA',
    # Pergunta 4
    f'{fvm}>>>  O que é gôndola?   {sc}'
    f'\n{am}A) {br}EMBARCAÇÃO'
    f'\n{am}B) {br}BRINQUEDO'
    f'\n{am}C) {br}MÚSICA'
    f'\n{am}D) {br}SÍMBOLO',
    # Pergunta 5
    f'{fvm}>>>  Como é chamada a cantora que representa o papel principal em uma ópera?   {sc}'
    f'\n{am}A) {br}PRIMEIRA DAMA'
    f'\n{am}B) {br}DONA-PRIMA'
    f'\n{am}C) {br}PRIMA-DONA'
    f'\n{am}D) {br}OBRA-PRIMA',
    # Pergunta 6
    f'{fvm}>>>  Que rio corta a cidade de Londres, na Inglaterra?   {sc}'
    f'\n{am}A) {br}TÂMISA'
    f'\n{am}B) {br}SENA'
    f'\n{am}C) {br}RENO'
    f'\n{am}D) {br}AUBE',
    # Pergunta 7
    f'{fvm}>>>  Qual cantor ficou conhecido como “O rei da voz”?   {sc}'
    f'\n{am}A) {br}ORLANDO SILVA'
    f'\n{am}B) {br}VICENTE CELESTINO'
    f'\n{am}C) {br}FRANCISCO ALVES'
    f'\n{am}D) {br}CARLOS GALHARDO',
    # Pergunta 8
    f'{fvm}>>>  Quantos quilates tem o ouro puro?   {sc}'
    f'\n{am}A) {br}18'
    f'\n{am}B) {br}20'
    f'\n{am}C) {br}24'
    f'\n{am}D) {br}30',
    # Pergunta 9
    f'{fvm}>>>  De quantos em quantos anos aparece o cometa Halley?   {sc}'
    f'\n{am}A) {br}57 ANOS'
    f'\n{am}B) {br}67 ANOS'
    f'\n{am}C) {br}76 ANOS'
    f'\n{am}D) {br}79 ANOS'
],
    'resposta':['D', 'B', 'D', 'C', 'A', 'C', 'A', 'C', 'C', 'C',]
}

nivel3 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 1
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 2
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 3
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 4
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 5
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 6
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 7
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 8
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 9
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg'
],
    'resposta':['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
}

nivel4 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 1
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 2
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 3
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 4
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 5
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 6
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 7
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 8
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg',
    # Pergunta 9
    f'{fvm}>>>  msg   {sc}'
    f'\n{am}A) {br}msg'
    f'\n{am}B) {br}msg'
    f'\n{am}C) {br}msg'
    f'\n{am}D) {br}msg'
],
    'resposta':['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
}

# Foi criado esse dicionário para serem usadas quando o jogador quiser pular no jogo, assim evito a repetição;
pulos = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Qual personagem da turma da Mônica tem apenas cinco fios de cabelo?   {sc}'
    f'\n{am}A) {br}MÔNICA'
    f'\n{am}B) {br}CEBOLINHA'
    f'\n{am}C) {br}CASCÃO'
    f'\n{am}D) {br}MAGALI',
    # Pergunta 1
    f'{fvm}>>>  Qual cantora tinha o apelido de “Ternurinha” na época da jovem guarda?   {sc}'
    f'\n{am}A) {br}SILVINHA'
    f'\n{am}B) {br}WANDERLÉIA'
    f'\n{am}C) {br}GRETCHEN'
    f'\n{am}D) {br}MARTINHA',
    # Pergunta 2
    f'{fvm}>>>  Quantas dentições naturais tem o ser humano durante a vida?   {sc}'
    f'\n{am}A) {br}UMA'
    f'\n{am}B) {br}DUAS'
    f'\n{am}C) {br}TRÊS'
    f'\n{am}D) {br}QUATRO',
    # Pergunta 3
    f'{fvm}>>>  Quantos dias tem um ano bissexto?   {sc}'
    f'\n{am}A) {br}364'
    f'\n{am}B) {br}365'
    f'\n{am}C) {br}366'
    f'\n{am}D) {br}367',
    # Pergunta 4
    f'{fvm}>>>  Quem foi técnico da Seleção brasileira de futebol na Copa de 98?   {sc}'
    f'\n{am}A) {br}ZAGALLO'
    f'\n{am}B) {br}SCOLARI'
    f'\n{am}C) {br}LUXEMBURGO'
    f'\n{am}D) {br}CARPEGIANNI',
    # Pergunta 5
    f'{fvm}>>>  O dromedário tem quantas corcovas?   {sc}'
    f'\n{am}A) {br}UMA'
    f'\n{am}B) {br}DUAS'
    f'\n{am}C) {br}TRÊS'
    f'\n{am}D) {br}QUATRO',
    # Pergunta 6
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 7
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 8
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 9
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 10
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 11
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 12
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 13
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 14
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
    # Pergunta 15
        f'{fvm}>>>  msg   {sc}'
        f'\n{am}A) {br}msg'
        f'\n{am}B) {br}msg'
        f'\n{am}C) {br}msg'
        f'\n{am}D) {br}msg',
],
    
    'resposta': ['B', 'B', 'B', 'C', 'A', 'A', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
}


# Essa função faz com que o sorteio não se repita; Lembrando que a ordem do sorteio corresponde a ordem das perguntas;
sorteio = []
while len(sorteio) != len(nivel1['pergunta']):
    r = randint(0, len(nivel1['pergunta']) -1)
    if r not in sorteio:
        sorteio.append(r)

# O mesmo ocorre para as perguntas da função pular;
pular = []
while len(pular) != len(pulos['pergunta']):
    r = randint(0, len(pulos['pergunta']) - 1)
    if r not in pular:
        pular.append(r)


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
                    linha()
                    print(f'A RESPOSTA CORRETA É A OPÇÃO: {am}{resposta}{br}')
                    sair()
                    break
            elif resp2 == 'N':
                continue
            else:
                erro(f'ERRO! dados inválidos, digite apenas {am}S{br} ou {am}N{br}.')
    elif escolha == 'A':
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
            erro('ERRO! dados inválidos, digite corretamente!')


def rodada1():
    """
    P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
        será escolhida.
    pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
        indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
        repetem, isso é feito na variável sorteio em variáveis globais).
    resposta: Ocorre o mesmo que na pergunta.
    cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
        chamada moeda, apenas para converter inteiro para o formato dinheiro.
    SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
        aúdio está.
    :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
        posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
        rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
        recurso da ajuda pular.
    """
    p = 0
    pergunta = nivel1['pergunta'][sorteio[0]]
    resposta = nivel1['resposta'][sorteio[0]]
    cabecalho(f' 1ª PERGUNTA, VALENDO {moeda(valor[0])} REAIS')
    placar()
    som('audio/frase_1mil.mp3')
    perguntas(pergunta, resposta, rodada2, p)


def rodada2():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 1
    pergunta = nivel1['pergunta'][sorteio[1]]
    resposta = nivel1['resposta'][sorteio[1]]
    cabecalho(f' 2ª PERGUNTA, VALENDO {moeda(valor[1])} REAIS')
    placar()
    som('audio/frase_2mil.mp3')
    perguntas(pergunta, resposta, rodada3, p)


def rodada3():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 2
    pergunta = nivel1['pergunta'][sorteio[2]]
    resposta = nivel1['resposta'][sorteio[2]]
    cabecalho(f' 3ª PERGUNTA, VALENDO {moeda(valor[2])} REAIS')
    placar()
    som('audio/frase_3mil.mp3')
    perguntas(pergunta, resposta, rodada4, p)


def rodada4():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 3
    pergunta = nivel1['pergunta'][sorteio[3]]
    resposta = nivel1['resposta'][sorteio[3]]
    cabecalho(f' 4ª PERGUNTA, VALENDO {moeda(valor[3])} REAIS')
    placar()
    som('audio/frase_4mil.mp3')
    perguntas(pergunta, resposta, rodada5, p)


def rodada5():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 4
    pergunta = nivel1['pergunta'][sorteio[4]]
    resposta = nivel1['resposta'][sorteio[4]]
    cabecalho(f' 5ª PERGUNTA, VALENDO {moeda(valor[4])} REAIS')
    placar()
    som('audio/frase_5mil.mp3')
    perguntas(pergunta, resposta, rodada6, p)


def rodada6():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 5
    pergunta = nivel2['pergunta'][sorteio[0]]
    resposta = nivel2['resposta'][sorteio[0]]
    cabecalho(f' 6ª PERGUNTA, VALENDO {moeda(valor[5])} REAIS')
    placar()
    som('audio/frase_10mil.mp3')
    perguntas(pergunta, resposta, rodada7, p)


def rodada7():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 6
    pergunta = nivel2['pergunta'][sorteio[1]]
    resposta = nivel2['resposta'][sorteio[1]]
    cabecalho(f' 7ª PERGUNTA, VALENDO {moeda(valor[6])} REAIS')
    placar()
    som('audio/frase_20mil.mp3')
    perguntas(pergunta, resposta, rodada8, p)


def rodada8():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 7
    pergunta = nivel2['pergunta'][sorteio[2]]
    resposta = nivel2['resposta'][sorteio[2]]
    cabecalho(f' 8ª PERGUNTA, VALENDO {moeda(valor[7])} REAIS')
    placar()
    som('audio/frase_30mil.mp3')
    perguntas(pergunta, resposta, rodada9, p)


def rodada9():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 8
    pergunta = nivel2['pergunta'][sorteio[3]]
    resposta = nivel2['resposta'][sorteio[3]]
    cabecalho(f' 9ª PERGUNTA, VALENDO {moeda(valor[8])} REAIS')
    placar()
    som('audio/frase_40mil.mp3')
    perguntas(pergunta, resposta, rodada10, p)


def rodada10():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 9
    pergunta = nivel2['pergunta'][sorteio[4]]
    resposta = nivel2['resposta'][sorteio[4]]
    cabecalho(f' 10ª PERGUNTA, VALENDO {moeda(valor[9])} REAIS')
    placar()
    som('audio/frase_50mil.mp3')
    perguntas(pergunta, resposta, rodada11, p)


def rodada11():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 10
    pergunta = nivel3['pergunta'][sorteio[0]]
    resposta = nivel3['resposta'][sorteio[0]]
    cabecalho(f' 11ª PERGUNTA, VALENDO {moeda(valor[10])} REAIS')
    placar()
    som('audio/frase_100mil.mp3')
    perguntas(pergunta, resposta, rodada12, p)


def rodada12():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 11
    pergunta = nivel3['pergunta'][sorteio[1]]
    resposta = nivel3['resposta'][sorteio[1]]
    cabecalho(f' 12ª PERGUNTA, VALENDO {moeda(valor[11])} REAIS')
    placar()
    som('audio/frase_200mil.mp3')
    perguntas(pergunta, resposta, rodada13, p)


def rodada13():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 12
    pergunta = nivel3['pergunta'][sorteio[2]]
    resposta = nivel3['resposta'][sorteio[2]]
    cabecalho(f' 13ª PERGUNTA, VALENDO {moeda(valor[12])} REAIS')
    placar()
    som('audio/frase_300mil.mp3')
    perguntas(pergunta, resposta, rodada14, p)


def rodada14():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 13
    pergunta = nivel3['pergunta'][sorteio[3]]
    resposta = nivel3['resposta'][sorteio[3]]
    cabecalho(f' 14ª PERGUNTA, VALENDO {moeda(valor[13])} REAIS')
    placar()
    som('audio/frase_400mil.mp3')
    perguntas(pergunta, resposta, rodada15, p)


def rodada15():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 14
    pergunta = nivel3['pergunta'][sorteio[4]]
    resposta = nivel3['resposta'][sorteio[4]]
    cabecalho(f' 15ª PERGUNTA, VALENDO {moeda(valor[14])} REAIS')
    placar()
    som('audio/frase_500mil.mp3')
    perguntas(pergunta, resposta, rodada16, p)


def rodada16():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    p = 15
    pergunta = nivel4['pergunta'][sorteio[0]]
    resposta = nivel4['resposta'][sorteio[0]]
    cabecalho(f' PERGUNTA FINAL, VALENDO {moeda(valor[15])} REAIS')
    placar()
    som('audio/frase_final.mp3')
    perguntas(pergunta, resposta, final, p)


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
            print('Placar do jogo') #placar(arq)
        elif resp == 'C':
            print('Regras do jogo') #regras()
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

def final():
    print('Final do jogo')
    
    
# ===================== FUNÇÕES DO SISTEMA ============================================================================
def layout():
    print(br)
    linha('=')
    print(f'|{am+"JOGO SHOW DO MILHÃO - V1.0".center(78)+br}|')
    linha('=')
    print(f'|{am+"BEM VINDO AO JOGO SHOW DO MILHÃO!".center(78)+br}|')
    linha('=')
    print(f'|{az}{"Acerte as perguntas e concorra ao premio de R$ 1.000,000,00 de reais".center(78)}{br}|')
    linha('=')
    placar()

def placar():
    print(f'| {am}{" AJUDAS DO JOGO >>> "}{br} | {"PULAR: "} {am}{pulo}{br} | {"CARTAS: "} {am}{cartas}{br} | {"CONVIDADOS: "} {am}{convidados}{br} | {"COLEGAS: "} {am}{colegas}{br} |')
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


def moeda(premio, moeda='R$ '):
    return f'{moeda}{premio:.2f}'.replace('.', ',')


# ===================== INÍCIO DO PROGRAMA ============================================================================
inicio()
#pula(nivel1)


