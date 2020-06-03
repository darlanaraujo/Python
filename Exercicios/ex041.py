'''
DESAFIO 041

A Confederação Nacional de Natação precisa de um programa que
LEIA O ANO DE NASCIMENTO de um atleta e MOSTRE SUA CATEGORIA
de acordo com a IDADE:

ATÉ 9 ANOS: MIRIM
ATÉ 14 ANOS: INFANTIL
ATÉ 19 ANOS: JUNIOR
ATÉ 20 ANOS: SENIOR
ACIMA: MASTER
'''

from datetime import date
data_atual = date.today().year

print('{}{}{}'.format('|', '='*100, '|'))
print('{}{:^100}{}'.format('|', 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO', '|'))
print('{}{}{}'.format('|', '='*100, '|'))
print('{}{:^100}{:>9}'.format('|', '\033[33mInforme abaixo os dados do atleta para saber a sua categora.\033[m', '|'))
print('{}{}{}'.format('|', '='*100, '|'))
nome = str(input('Nome do atleta: '.upper())).strip()
print('='*40)
ano = int(input('informe o ano de nascimento: '.upper()))
print('{}{}{}'.format('|', '='*100, '|'))
idade = data_atual - ano
if idade <= 9:
    categoria = 'mirin'
elif idade <= 14:
    categoria = 'infantil'
elif idade <= 19:
    categoria = 'junior'
elif idade == 20:
    categoria = 'senior'
else:
    categoria = 'master'
print('nome do atleta: {} \nidade do atleta: {} \ncategoria do atleta: {}'.upper().format(nome, idade, categoria).upper())
print('{}{}{}'.format('|', '='*100, '|'))
print('{}{:^100}{}'.format('|', 'FIM DO PROGRAMA', '|'))
print('{}{}{}'.format('|', '='*100, '|'))
