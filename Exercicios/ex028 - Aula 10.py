'''
Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5. E peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

dic={1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]} #Dicionário com os números a ser pensado pelo computador!
print('{:=^80}'.format(' EXERCICIO 28 '))
print()

import random #Função que sorteia a ordem

index=random.randint(0,11)+1 #Aqui define que o indice vai de 0 a 10

print('Desafio você adivinhar o numero que estou pensando!')
print()
print('Suas opções vão de 0 a 10')
resposta=str(input('Vamos jogar? ')).lower().strip()[0]
if resposta == 's':
    print('=) Oba! Vamos começar!')
    pensamento=(dic[1][index]) #Aqui defino o número que será pensado pela maquina.
    print(pensamento) #Função temporária, apenas para testar o jogo e saber qual número foi pensado!
    print()
    n1=int(input('Qual número estou pensando agora? '))
    if (pensamento == n1): #Aqui comparo o numero pensado com o número escolhido pelo jogador.
        print('O numero que pensei foi o: {}'.format(pensamento))
        print()
        print('Nossa! Você acertou. Meu Parabéns!')
    else:
        print('O número que pensei foi o: {}'.format(pensamento))
        print()
        print('Ah! Que pena, você errou.')
else:
   print('Que pena, você desistiu do jogo!')
print()
print('{:=^80}'.format(' !!! FIM DO JOGO !!! '))

'''print('{:=^40}'.format('EXERCICIO 028'))
print()
numero = 4
print('Desafio você a adivinhar o numero que estou pensando!')
print('Suas opções são de 0 a 5')
resposta=str(input('Vamos jogar? ')).lower()
if 'sim'in resposta:
    print(':) Oba! Vamos começar!')
    n1=str(input('Qual número estou pensando? '))
    if '4' in n1:
        print('MEUS PARABÉNS! Você acertou')
    else:
        print('Que pena! Você não acertou')
        print('O numero que estava pensando era {}'.format(numero))
else:
    print('Que pena! Você não quer jogar :(')
print()
print('{:=^40}'.format('FIM DO PROGRAMA'))'''
