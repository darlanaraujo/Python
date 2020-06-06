'''
DESAFIO 094

Crie um programa que LEIA NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa em um
DICIONÁRIO e todos os dicionário em uma LISTA. No final, mostre:

A) QUANTAS PESSOAS FORAM CADASTRADAS;
B) A MÉDIA DE IDADE DO GRUPO;
C) UMA LISTA COM TODAS AS MULHERES;
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA.
'''
# ================= MODELO CRIADO =====================================================================================
pessoas = {}
dados = []
media = soma = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).title().strip()
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    dados.append(pessoas.copy())
    print('='*50)

    resp = str(input('Continuar cadastrando? [S/N]: '))
    if resp in 'nN':
        break
    print('='*50)

media = soma / len(dados)
print('='*50)
print(f'{"RELATÓRIO DOS DADOS":^50}')
print('='*50)
print(f'A) Foram cadastradas {len(dados)} pessoas')
print(f'B) A média de idade do grupo: {media:.1f} anos')
print(f'C) Lista das mulheres cadastradas: ', end= '')

for p, d in enumerate(dados):
    if dados[p]['sexo'] == 'F':
        print(f'{dados[p]["nome"]}', end=' ')
print('\nD) Pessoas com idade acima da média: ', end='')
for p, d in enumerate(dados):
    if dados[p]['idade'] > media:
        print(f'{dados[p]["nome"]}', end=' ')

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
