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
'''pessoas = {}
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
        print(f'{dados[p]["nome"]}', end=' ')'''

# ================= MELHORIA DO CÓDIGO ================================================================================
pessoas = {}
dados = []

def inicio(msg):
    cabecalho(msg)
    cadastro()


def cabecalho(msg):
    print('\033[30m-='*30)
    print(f'\033[33m{msg:^60}\033[30m')
    print('-='*30)


def sexo():
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('\033[31mATENÇÃO! \033[30mDados inválidos. Digite corretamente!\033[30m')


def cadastro():
    pessoas['nome'] = str(input('Nome: ')).title().strip()
    sexo()
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())
    loop('\033[33mContinuar o cadastrando? [S/N]:\033[30m ', 'sS', 'nN')


def loop(msg, sim, nao):
    print('-='*30)
    while True:
        resp = str(input(msg))
        if resp in sim:
            print('-=' * 30)
            return cadastro()
        elif resp in nao:
            relatorio()
            break
        else:
            print('\033[31mATENÇÃO! \033[30mDados inválidos. Digite corretamente!\033[30m')


def relatorio():
    soma = 0
    cabecalho('RELATÓRIO DE DADOS')
    print(f'A) NÚMERO DE PESSOAS CADASTRADAS: \033[33m{len(dados)}\033[30m')

    for p, v in enumerate(dados):
        soma += dados[p]['idade']
    media = soma / len(dados)
    print(f'B) MÉDIA DE IDADE DO GRUPO: \033[33m{media}\033[30m')

    print(f'C) MULHERES CADASTRADAS:', end=' ')
    for p, v in enumerate(dados):
        if dados[p]['sexo'] == 'F':
            print(f'\033[33m{dados[p]["nome"]}\033[30m', end=' ')
    print()
    print(f'D) PESSOAS COM IDADE ACIMA DA MÉDIDA:')
    for p, v in enumerate(dados):
        if dados[p]['idade'] > media:
            print(f'    >>> Nome \033[33m{dados[p]["nome"]}\033[30m, Idade: \033[33m{dados[p]["idade"]}\033[30m')
    print('-='*30)


inicio('CADASTRO DE PESSOAS')

# ================= ANÁLISE DO CÓDIGO ================================================================================
'''
Comparando os dois códigos base, os comandos e a forma de pensar foi muito parecido, porem o código do curso aplicou
algumas funções melhores, como corrigindo possiveis erros de digitação. Entre eles destaco o uso invertido do break
junto com while, já que ele para o loop quando a informação está correta e não quando há uma negação.

O código aprimorado eu usei recursos mais avançados, poderia ter feito funções até melhores, mas para cumprimento do
enunciado foram suficientes.
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
'''pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responta apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')'''