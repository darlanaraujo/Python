'''
DESAFIO 059

Crie um programa que LEIA DOI VALORES e mostre um MENU NA TELA

[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

Seu programa deverá REALIZAR A OPERAÇÃO solicitado em cada caso.
'''

from time import sleep

#
stop = 'sair'
resposta = ''

#Inicio do programa
n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
print('=-'*30)

#Inicio do laço
while stop != resposta:

    print('Escolha o que deseja fazer com os valores que digitou.')
    print('''
    [1] SOMAR:
    [2] MULTIPLICAR:
    [3] MAIOR VALOR:
    [4] DIGITAR OUTROS NÚMEROS:
    [5] SAIR DO PROGRAMA:
    ''')
    resposta = str(input('>>>: ')).lower().strip()

    #Comando para somar
    if resposta == 'somar' or resposta == '1':
        soma = n1 + n2
        print('A soma entre {} + {} é = {}'.format(n1, n2, soma))


    #Comando para multiplicar
    elif resposta == 'multiplicar' or resposta == '2':
        soma = n1 * n2
        print('A soma de {} x {} é = {}'.format(n1, n2, soma))


    #Comando para identificar o maior numero
    elif 'maior' in resposta or resposta == '3':
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o MAIOR número é {}'.format(n1, n2, maior))


    # Comando para escolher outro número
    elif 'digitar' in resposta or resposta == '4':
        print('Ok. Digite novamente os valores.')
        print('-='*30)
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite o segundo número: '))
        print('Atualizando os novos valores...')


    #Comando para sair do programa
    elif resposta == 'sair' or resposta == '5':
        print('...Finalizando o programa!')
        resposta = stop


    #Comando de erro para valores errados
    else:
        print('Opção invalida. Digite novamente.')

    #Reinicio do laço com um atraso de 2 segundos
    print('-='*30)
    sleep(2)

#Fim do programa
print('Fim do programa!')
