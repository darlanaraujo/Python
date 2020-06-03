'''
DESAFIO 058 - AULA 14

MELHORE O JOGO DO DESAFIO 028 aonde o computador vai PENSAR EM UM NÚMERO DE 0 a 10.
Só que agora O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, mostrando no FINAL quantos
PALPITES FORAM NECESSÁRIOS para vencer.

'''

# ================== INÍCIO COM PROGRAMA ==============================================================

# Função de importação;
from random import randint
from time import sleep

# ================= VARIAVEIS GLOBAIS ==================================================================
maquina = 0
sorteio = 100

# Contadores
erros = 0
acertos = 0

# Variável comparativo da maquina com o jogador
acertou = False

# Função de sorteio dos números;
maquina = randint(0, 10)

print(maquina) #Função de teste para ver o número sorteado.

# ====================== LAYOUT DO PROGRAMA ==============================================================

print('|'+'-='*25+'|')
print('{}\033[33m{:^50}\033[m{}'.format('|', 'JOGO DE ADIVINHAÇÃO', '|'))
print('|'+'=-'*25+'|')
print('{}\033[30m{:^50}\033[m{}'.format('|', 'VOU PENSAR EM UM NÚMERO DE 0 A 10', '|'))
print('{}\033[33m{:^50}\033[m{}'.format('|', 'TENTE ADIVINHAR!', '|'))
print('|'+'=-'*25+'|')
print('{}\033[30m{:^50}\033[m{}'.format('|', 'HUMMMM! DEIXA EU PENSAR =)...', '|'))
for c in range(0, 11):
    print('|', end=' ')
    print('\033[30m{}\033[m'.format(c), end=' '), sleep(0.5)
print('      |')
sleep(0.5)
print('{}\033[33m{:^50}\033[m{}'.format('|', ' JÁ PENSEI EM UM NÚMERO!', '|'))
sleep(0.5)

''''# ====================== DEFINIÇÃO DE ERRO ===============================================================

def alerta():
    erro = '{}{:^58}{}'.format('|', '\033[31mATENÇÃO! Digite o comando correto [S/N]\033[m', '|')

    resposta = str(input('| \033[30mDeseja continuar jogando? [S/N]:\033[m ')).upper().strip()
    print('{}{}{}'.format('|', '=-' * 25, '|'))


    return erro, resposta'''

# ======================LAÇO DE REPETIÇÃO DAS PERGUNTAS ==================================================
while not acertou:
    sorteio = int(input('| \033[30mTENTE ADIVINHAR DE 0 A 10 >>>\033[m '))
    print('{}{}{}'.format('|', '=-'*25, '|'))
    if sorteio != maquina:
        print('{}\033[31m{:^50}\033[m{}'.format('|', 'Você ERROU! Continue tentando.', '|'))
        erros += 1
    else:
        print('{}\033[33m{:^50}\033[m{}'.format('|', 'PARABÉNS! Você acertou', '|'))
        acertos += 1
        print('{}{}{}'.format('|', '-='*25, '|'))

    # Reinicio do jogo.

        resposta = str(input('| \033[30mDeseja continuar jogando? [S/N]:\033[m ')).upper().strip()[0]
        print('{}{}{}'.format('|', '=-' * 25, '|'))

        # Repetição da pergunta caso a resposta seja incorreta.
        while resposta not in 'SN':
            print('{}{:^58}{}'.format('|', '\033[31mATENÇÃO! Digite o comando correto [S/N]\033[m', '|'))
            resposta = str(input('| \033[30mDeseja continuar jogando? [S/N]:\033[m ')).upper().strip()[0]
            print('{}{}{}'.format('|', '=-' * 25, '|'))

        if resposta == 'S':

            print('{}\033[30m{:^50}\033[m{}'.format('|', 'DEIXA EU PENSAR EM OUTRO NÚMERO =)', '|'))
            for c in range(0, 11):
                print('{}\033[30m{}\033[m'.format('| ', c), end= ' '), sleep(0.5)
            print('      |')
            maquina = randint(0, 10)
            print('{}\033[33m{:^50}\033[m{}'.format('|', 'JÁ PENSEI!', '|'))
            #print(maquina) #Função de teste apenas para ver o número sorteado.
            sorteio = int(input('| \033[30mTENTE ADIVINHAR! DE 0 A 10 >>>\033[m '))
            print('{}{}{}'.format('|', '=-'*25, '|'))

            if sorteio != maquina:
                print('{}\033[31m{:^50}\033[m{}'.format('|', 'VOCÊ ERROU! Continue tentando.', '|'))
                erros += 1
            else:
                print('{}\033[33m{:^50}\033[m{}'.format('|', 'PARABÉNS! Você acertou.', '|'))
                acertos += 1
            print('{}{}{}'.format('|', '-='*25, '|'))
        elif resposta == 'N':
            break


jogadas = erros + acertos
print('{}\033[33m{:^50}\033[m{}'.format('|', 'RELATÓRIO DO JOGO', '|'))
print('{}{}{}'.format('|', '=-'*25, '|'))
print('{}\033[33m{}\033[30m{}\033[m{:>32}'.format('|', 'TOTAL DE JOGADAS: ', jogadas, '|'))
print('{}{:>51}'.format('|', '|'))
print('{}\033[30m{}\033[31m{}\033[m{:>34}'.format('|', 'TOTAL DE ERROS: ', erros, '|'))
print('{}\033[30m{}\033[33m{}\033[m{:>32}'.format('|', 'TOTAL DE ACERTOS: ', acertos, '|'))
print('{}{}{}'.format('|', '=-'*25, '|'))
print('{}\033[33m{:^50}\033[m{}'.format('|', 'FIM DO JOGO', '|'))
print('{}{}{}'.format('|', '-='*25, '|'))
