'''
DESAFIO 107

Crie um módulo chamado moedas.py que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() E METADE().

Faça também um programa que IMPORTE esse módulo e use algumas dessas funções.
'''
# ============= CÓDIGO BASE ===========================================================================================
from modulos import moedas

'''num = float(input('Digite o Preço: R$ '))
print(f'O valor de {num} com aumento de 10% é = {moedas.aumentar(num, 10)}')
print(f'O valor de {num} menos 13% é = {moedas.diminuir(num, 13)}')
print(f'O valor de {num} dobrado é = {moedas.dobro(num)}')
print(f'O valor da metade de {num} é = {moedas.metade(num)} ')'''

# ============= CÓDIGO APRIMORADO =====================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
A criação desse código é bem fácil e ambos os códigos são parecidos. A análise mais detalhada está dentro do módulo
aonde as funções foram criadas.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é R$ {moedas.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moedas.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moedas.aumentar(p, 10)}')