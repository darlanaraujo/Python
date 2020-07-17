# ======================= FUNÇÕES GLOBAIS DO JOGO =====================================================================
from random import randint
from modulos.lib.showmilhao import *

pergunta_niv1 = ['Qual o meu nome? \nA) Darlan Araujo \nB) Fabil Santana \nC) Antônio Silva \nD) José Pereira',
                 'Qual cidade eu nasci? \nA) Eunápolis \nB) Itamaraju \nC) Nova Alegria \nD) Além Paraíba',
                 'Qual a minha idade? \nA) 17 anos \nB) 24 anos \nC) 30 anos \nD) 35 anos',
                 ]

resposta_niv1 = ['A',
                 'B',
                 'D',
                 ]

sorteio = randint(0, 2)


# ======================= FUNÇÕES DE PERGUNTAS DO JOGO ================================================================
def capa():
    cabeçalho('=', 'PRIMEIRA RODADA VALENDO R$ 1.000,00 REAIS')
    while True:
        resp = str(input('VAMOS SOMEÇAR? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            perguntas()
        elif resp == 'N':
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
            erro('ERRO! Escolha uma opção válida!')


def perguntas():
    pergunta1 = pergunta_niv1[sorteio]
    resposta1 = resposta_niv1[sorteio]

    # FERRAMENTA DE TESTE
    print(resposta1)

    print(f'Vamos ao primeiro nivel do jogo, com a primeira pergunta')
    print(pergunta1)
    resp = str(input('Escolha a opção correta: ')).upper().strip()[0]
    if resp == resposta1:
        print('PARABÉNS! Você acertou.')
    else:
        print('Que pena, você errou!')
