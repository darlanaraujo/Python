'''
DESAFIO 108

Adapte o código do DESAFIO 107, criando uma função adicional chamada MOEDA() que consiga mostrar os valores como um
valor monetário formatado.
'''
# ============= CÓDIGO BASE ===========================================================================================
from modulos import moedas

'''num = float(input('Digite o preço: R$ '))
print(f'O valor de {moedas.moeda(num)} com aumento de 10% é = {moedas.moeda(moedas.aumentar(num, 10))}')
print(f'O valor de {moedas.moeda(num)} menos 13% é = {moedas.moeda(moedas.diminuir(num, 13))}')
print(f'O valor de {moedas.moeda(num)} dobrado é = {moedas.moeda(moedas.dobro(num))}')
print(f'O valor da metade de {moedas.moeda(num)} é = {moedas.moeda(moedas.metade(num))} ')'''

# ============= CÓDIGO APRIMORADO =====================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
A criação desse código é bem fácil e ambos os códigos são parecidos. A análise mais detalhada está dentro do módulo
aonde as funções foram criadas.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é R$ {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é R$ {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')