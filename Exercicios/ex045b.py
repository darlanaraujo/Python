'''
DESAFIO 045

Crie um programa que faça o COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

'''
#Dicionário para importação do conteudo.
dic = {1: ['pedra', 'papel', 'tesoura']}

#Função random para importar do dicionário.
import random

#Comando de importação e definição de variável.
index = random.randint(0,2)
maquina = (dic[1][index])

print('\033[30m#'*180)
print('#\033[m'*180)
print('{:^180}'.format('\033[1;4;33mBEM VINDO AO JOGO DE JOKEPÔ\033[m'))
print()
print('\033[31mAS REGRAS DO JOGO:\033[m')
print('\033[33mPAPEL \033[30mquebra a \033[33mTESOURA; \n\033[33mTESOURA \033[30mcorta o \033[33mPAPEL; \n\033[33mPAPEL \033[30mcobre a \033[33mPEDRA;')
print()
print('\033[30mPARA INICIAR BASTA FAZER A SUA JOGADA!')
print()
jogador = str(input('PODE COMEÇAR: ')).lower().strip()
if jogador in 'pedra papel tesoura':
    print('A MAQUINA JOGA: \033[31m{}\033[m'.format(maquina).upper())
else:
    print('\033[31mATENÇÃO! Use as palavras corretas do jogo. PEDRA - PAPEL - TESOURA')
    print('#'*40)
    print()
    jogador = str(input('\033[30mJOGUE NOVAMENTE: ')).lower().strip()
    print('A MAQUINA JOGA: \033[31m{}\033[m'.format(maquina).upper())
if maquina == 'papel' and jogador == 'pedra' or maquina == 'pedra' and jogador == 'tesoura' or maquina == 'tesoura' and jogador == 'papel':
    print('#'*40)
    print('\033[31mA MAQUINA VENCEU!')
    print('#'*40)
elif jogador == 'papel' and maquina == 'pedra' or jogador == 'pedra' and maquina == 'tesoura' or jogador == 'tesoura' and maquina == 'papel':
    print('#'*40)
    print('\033[32mO JOGADOR VENCEU!')
    print('#'*40)
elif jogador == 'papel' and maquina == 'papel' or jogador == 'pedra' and maquina == 'pedra' or jogador == 'tesoura' and maquina == 'tesoura':
    print('#'*40)
    print('\033[34mO JOGO EMPATOU! JOGUEM NOVAMENTE.')
    print('#'*40)
else:
    print()
    print('\033[31m#'*70)
    print('A palavra que usou \033[30m{} \033[31mnão faz parte do jogo!'.format(jogador.upper()))