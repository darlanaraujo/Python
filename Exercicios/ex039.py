'''
DESAFIO 039

Faça um programa que LEIA O ANO DE NASCIMENTO de uma pessoa e informe, de
acordo com sua idade:

Se ele AINDA VAI SE ALISTAR ao serviço militar.
Se já é HORA DE SE ALISTAR.
Se já PASSOU DO TEMPO DO ALISTAMENTO.

o programa também deverá MOSTRAR O TEMPO QUE FALTA OU O TEMPO QUE PASSOU DO PRAZO.

'''

def cabecalho():
    print('|', '='*100, '|')
    print('{}{:^112}{}'.format('|', '\033[1;33mSISTEMA DE ALISTAMENTO MILITAR\033[m', '|'))
    print('|', '='*100, '|')

def corpo():
    print('|', ' '*100, '|')

from datetime import date
ano_atual = date.today().year

cabecalho()
print('SEJA BEM VINDO(A) AO SISTEMA DE ALISTAMENTO MILITAR.')
print('Para saber qual a sua condição de alistamento, preencha os dados abaixo.'.upper())
print()
nome = str(input('informe o nome: '.upper())).upper().strip()
print('='*50)
sexo = str(input('informe o sexo: '.upper())).lower().strip()
print('='*50)
if sexo == 'masculino' or sexo == 'homem':
    idade = int(input('informe o ano de nascimento: '.upper()))
    soma = ano_atual - idade
    if soma == 18:
        print('você tem {} anos, chegou o momento de se alistar! Procure a junta militar mais próxima.'.format(soma).upper())
    elif soma < 18:
        print('você tem {} anos, ainda falta {} anos para se alistar!'.format(soma, 18-soma).upper())
    else:
        print('você tem {} anos, já passou {} anos do momento para se alistar. procure a junta militar para \nregularizar sua reservista.'.format(soma, soma-18).upper())
else:
    print('Você não é obrigado ao alistamento militar.'.upper())
print()
print('|', '='*100, '|')
print('{}{:^112}{}'.format('|', '\033[1;30mFIM DO PROGRAMA\033[m', '|'))
print('|', '='*100, '|')
