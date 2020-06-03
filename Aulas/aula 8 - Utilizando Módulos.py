'''
AULA 08 - UTILIZANDO MÓDULOS DE IMPORTAÇÃO

EXEMPLOS DE BIBLIOTECAS E SUA IMPORTAÇÃO.
Nome das Bibliotecas: BEBIDA - COMIDA - DOCE

Exemplo de como importar uma biblioteca;

import bebida #Nesse comando eu importaria tudo que estiver dentro da biblíoteca bebida.

from bebida import cafe, leite #Nesse comando eu importo apenas os itens desejados dentro da biblioteca escolhida.

Quando eu importo toda uma biblioteca para usar as funções dentro da biblioteca eu tenho que iniciarda seguinte forma.

import math #Aqui eu importei toda a biblioteca

math.função #aqui eu uso a biblioteca, e coloco um ponto, o programa me mostra uma lista com as funções da biblioteca,
basta escolher a função desejada.

PARA UTILIZAR AS BIBLIOTECAS PADRÃO DO PYTHON, É SÓ ACESSAR O SITE DO PYTHON

https://docs.python.org/3/library/index.html
'''

#Exemplo de um código para mostrar a raiz quadrada de um número de forma manual.
'''
num = int(input('Digite um número: '))
raiz = num ** (1/2)
print(raiz)
'''
# ================================================================================
# Agora utilizando uma biblioteca
'''
import math

num2 = int(input('Digite um número: '))
raiz2 = math.sqrt(num2)
print(raiz2)
'''
# ================================================================================
# Outro exemplo igual só que, importando apenas a função desejada;
'''
from math import floor, sqrt

num3 = int(input('Digite um número: '))
raiz3 = sqrt(num3)
print(floor(raiz3)) #A função floor arredonda o numero para baixo.
'''
# ================================================================================
# Importação da biblioteca randon para gerar resultados aleatórios;

import random
num = random.randint(0, 10) #A função randint() lê uma relação de números inteiros, nesse caso de 0 a 10
print(num)