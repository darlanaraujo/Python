'''
DESAFIO 109

Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um PARÂMETRO a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvido no DESAFIO 108.
'''
# ============= CÓDIGO BASE ===========================================================================================
from modulos import moedas

'''num = float(input('Digite o Preço: R$ '))
print(f'O valor de {moedas.moeda(num)} com aumento de 10% é = {moedas.aumentar(num, 10, True)}')
print(f'O valor de {moedas.moeda(num)} menos 13% é = {moedas.diminuir(num, 13, True)}')
print(f'O valor de {moedas.moeda(num)} dobrado é = {moedas.dobro(num, True)}')
print(f'O valor da metade de {moedas.moeda(num)} é = {moedas.metade(num, True)} ')'''

# ============= CÓDIGO APRIMORADO =====================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
A criação desse código é bem fácil e ambos os códigos são parecidos. A análise mais detalhada está dentro do módulo
aonde as funções foram criadas.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é R$ {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é R$ {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}')