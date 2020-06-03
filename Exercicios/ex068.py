'''
DESAFIO 068

Faça um programa que JOGUE PAR OU ÍMPAR com o computador.
O jogo só será interrompido quando o jogador PERDER,
mostrando o TOTAL DE VITÓRIAS CONSECUTIVAS que ele conquistou
no final do jogo.
'''
# ============= FUNÇÕES GERAIS DO PROGRAMA ===============================
import random

vitoria = cont = 0
tipo = ''
# ============= LAYOUT ===================================================
print(f'|{"="*30}|')
print(f'|\033[33m{"JOGO DE PAR OU ÍMPAR":^30}\033[m|')
print(f'|{"="*30}|')
# ============= INÍCIO DO PROGRAMA =======================================

# LAÇO DE REPETIÇÃO
while True:
    sorteio = random.randint(0, 10)
    n1 = int(input('| Escolha um número: '))
    print(f'|{"="*30}|')

    # CALCULOS DO JOGO
    soma = sorteio + n1
    resto = soma % 2
    cont += 1
    if resto == 0:
        resultado = 'PAR'
    if resto == 1:
        resultado = 'ÍMPAR'

    # ESCOLHA DO JOGADOR
    '''while tipo not in 'PIÍ':
        tipo = str(input('| Escolha PAR ou ÍMPAR')).upper().strip()[0]'''

    while True:
        jogador = str(input('| Esolha PAR ou ÍMPAR? ')).upper().strip()
        print(f'|{"="*30}|')
        if jogador == 'PAR':
            maquina = 'ÍMPAR'
            break
        elif jogador == 'ÍMPAR':
            maquina = 'PAR'
            break
        else:
            print(f'|\033[31m{"DADOS INVÁLIDOS":^30}\033[m|')

    print(f'| \033[30mVocê colocou: \033[33m{n1}\033[m')
    print(f'| \033[30mA Maquina colocou: \033[33m{sorteio}\033[m')
    print(f'| \033[30mO resultado foi: \033[33m{soma} = {resultado}\033[m')


    # ENQUANTO O JOGADOR GANHAR O JOGO CONTINUA
    if jogador == resultado:
        vitoria += 1
        print(f'|\033[33m{"PARABÉNS":^30}\033[m|')
        print(f'|{"Você acertou o resultado":^30}|')
        print(f'|\033[30m{"Vamos jogar novamente...":^30}\033[m|')
        print(f'|{"=" * 30}|')

    # SE O JOGADOR PERDER O JOGO PARA
    if jogador != resultado:
        print(f'|\033[31m{"QUE PENA VOCÊ PERDEU!":^30}\033[m|')
        print(f'|{"=" * 30}|')
        break

print(f'|\033[33m{"RESULTADO DO JOGO":^30}\033[m|')
if vitoria > 1:
    print(f'| Você jogou {cont} partidas \n| E ganhou {vitoria} vezes consecutivas')
elif vitoria == 1:
    print(f'| Você jogou {cont} partidas \n| E ganhou somente uma {vitoria} vez')
else:
    print(f'| Que pena! Você jogou apenas \n| {cont} partida e não venceu.')
print(f'|{"="*30}|')




