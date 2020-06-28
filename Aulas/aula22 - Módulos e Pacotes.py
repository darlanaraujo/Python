'''
AULA 22 - Módulos e Pacotes

Modularização: É uma forma de dividir o seu programa para que a leitura e manutenção do código fique mais fácil.

As principais vantagens são, organização do código; Facilidade na manutenção; Ocultação de códigos detalhados;
reutilização em outros projetos.

Pacotes (biblíoteca):
'''
# ============= PRÁTICA / TEORIA ======================================================================================

"""
Para criar um módulo o arquivo deve ter pelo menos duas funções. No modelo abaixo, temos 3 funções criadas, e posso
importalas sitando a pasta e o modulo. from pasta import modulo.
"""
# Modelo importando um item dentro do modulo
from modulos import uteis
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')



