'''
DESAFIO 109

Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um PARÂMETRO a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvido no DESAFIO 108.
'''
# ============= CÓDIGO BASE ===========================================================================================
from modulos import moedas

num = float(input('Digite o Preço: R$ '))
print(f'O valor de {moedas.moeda(num)} com aumento de 10% é = {moedas.aumentar(num, 10, True)}')
print(f'O valor de {moedas.moeda(num)} menos 13% é = {moedas.diminuir(num, 13, True)}')
print(f'O valor de {moedas.moeda(num)} dobrado é = {moedas.dobro(num, True)}')
print(f'O valor da metade de {moedas.moeda(num)} é = {moedas.metade(num, True)} ')

# ============= CÓDIGO APRIMORADO =====================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================

# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
