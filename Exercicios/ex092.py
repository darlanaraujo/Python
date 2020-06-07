'''
DESAFIO 092

Crie um programa que LEIA NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os
(COM IDADE) em um DICIONÁRIO se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO. Calcule e acrescente, além da
IDADE, com quantos anos a pessoa vai se APOSENTAR.
'''
# ===================== MODELO CRIADO =================================================================================
from datetime import date
dados = {}

dados['Nome'] = str(input('Nome completo: '))
ano = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano
print('\033[33mCaso não tenha carteira de trabalho, digite \033[30m0\033[m')
dados['CTPS'] = int(input('Numero da carteira: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário R$'] = float(input('Salário ganho: R$ '))
    dados['Aposentadoria'] = (dados['Contratação'] +35) - ano

print('='*40)
for itens in dados:
    print(f'{itens}: {dados[itens]}')

# ===================== MELHORIA DO CÓDIGO =============================================================================

# ===================== ANÁLISE DO CÓDIGO =============================================================================
'''
Os dois códigos são muito parecidos, algumas poucas diferenças, sendo a forma de usar a função datetime, no código
do curso achei muito desnecessário a quantidade de valores para chegar a um calculo de aposentadoria, o meu ficou mais
simples e funcionando do mesmo jeito. E no final a forma de organizar os dados.
'''
# ==================== MODELO CURSO EM VIDEO ==========================================================================
'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
'''