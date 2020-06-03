'''
DESAFIO 054

Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
No final, mostre QUANTAS PESSOAS AINDA NÃO ATIGIRAM A MAIORIDADE
E QUANTAS JÁ SÃO MAIORES.

**Considere maioridade aos 21 anos
'''

# =================== VARIÁVEIS GLOBAIS ===================================
from datetime import date

#idade = 0
maior = 0
menor = 0
ano = date.today().year

for c in range(1, 7 +1):
    nascimento = int(input('Em que ano nasceu a {}ª pessoa: '.format(c)))
    nascimento = ano - nascimento
    if nascimento < 21:
        menor += 1
    else:
        maior +=1
print('Você informou o ano de nascimento de {} pessoas.'.format(c))
if menor <=1:
    print('Sendo que {} tem menos que 21 anos. Por isso, NÃO ATINGIU A MAIORIDADE!'.format(menor))
    print('E {} tem mais que 21 anos. Por isso, ATINGIRAM A MAIORIDADE!'.format(maior))
else:
    print('Sendo que {} tem menos que 21 anos. Por isso, NÃO ATINGIRAM A MAIORIDADE!'.format(menor))
    print('E {} tem mais que 21 anos. Por isso ATINGIRAM A MAIORIDADE!'.format(maior))
