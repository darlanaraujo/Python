'''
DESAFIO 032

Faça um programa que leia um ano qualquer e mostra se
ele é um ano BISSEXTO.
'''

from datetime import date
#A função FROM diz que só pegara o conteudo selecionado
#
ano=int(input('Informe o ano que deseja analizar? Ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim! o ano {} é BISSEXTO.'.format(ano))
else:
    print('Não! o ano {} não é BISSEXTO.'.format(ano))