'''
DESAFIO 111

Crie um PACOTE chamado UTILIDADESCEV que tenha dois MÓDULOS INTERNOS chamados MOEDA e DADOS.

Transfira todas as funções utilizadas nos DESAFIOS 107, 108 E 109 para o primeiro pacote e mantenha tudo funcionando.
'''
# ============= CÓDIGO BASE ===========================================================================================
from modulos.utlidadesCeV import moeda

'''valor = float(input('Digite o preço: R$ '))
moeda.resumo(valor, 80, 35)'''
# ============= CÓDIGO APRIMORADO =====================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
A criação desse código é bem fácil e ambos os códigos são parecidos. A análise mais detalhada está dentro do módulo
aonde as funções foram criadas.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 80, 35)