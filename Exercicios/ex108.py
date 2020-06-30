'''
DESAFIO 108

Adapte o código do DESAFIO 107, criando uma função adicional chamada MOEDA() que consiga mostrar os valores como um
valor monetário formatado.
'''

from modulos import moedas

num = int(input('Digite um valor: '))
print(f'O valor de {num} com aumento de 10% é {moedas.aumentar(num)}')
print(f'O valor de {num} menos 25% é {moedas.diminuir(num)}')
print(f'O valor de {num} dobrado é {moedas.dobro(num)}')
print(f'O valor da metade de {num} é {moedas.metade(num)} ')