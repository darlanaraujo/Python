'''
DESAFIO 112

Dentro do pacote UTILIDADESCEV que criamos no DESAFIO 111, temos um MÓDULO chamado DADO. Crie uma função chamada
LEIADINHEIRO() que seja capaz de funcionar como a função INPUT(), mas com uma VALIDAÇÃO DE DADOS para aceitar apenas
valores que seja MONETÁRIOS.
'''
# ============= CÓDIGO BASE ===========================================================================================
from modulos.utlidadesCeV import dado, moeda

'''p = dado.leiadinheiro('Digite um valor: R$ ')'''

# ============= CÓDIGO APRIMORADO =====================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
A criação desse código é bem fácil e ambos os códigos são parecidos. A análise mais detalhada está dentro do módulo
aonde as funções foram criadas.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
p = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)