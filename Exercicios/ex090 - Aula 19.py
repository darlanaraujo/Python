'''
DESAFIO 090 - AULA 19 DICIONÁRIOS

Faça um programa que leia NOME E MÉDIA de um aluno, quardando também a SITUAÇÃO
em um DICIONÁRIO. No final, mostre o conteúdo da estrutura na tela.
'''
# ============== MODELO CRIADO ===========================================================================
'''relatorio = {'aprovado': 'Aprovado', 'recuperação': 'Recuperação', 'reprovado': 'Reprovado'}

nome = str(input('Nome: '))
media = float(input(f'Média do(a) {nome}: '))

print('='*50)
print(f'Aluno: {nome}')
print(f'Média: {media}')
if media <= 5:
    print(f'Situação: {relatorio["reprovado"]}')
elif media <= 6.9:
    print(f'Situação: {relatorio["recuperação"]}')
elif media >= 7:
    print(f'Situação: {relatorio["aprovado"]}')'''
# ============== MELHORIA DO CÓDIGO ======================================================================
'''
Apesar de ter coisas a serem melhoradas no cógido, optei por não fazer já que tem outro programa de coleta
de notas de alunos mais completo feito em uma aula anterior.
'''
# ============== ANÁLISE DO CÓDIGO =======================================================================
'''
Esse código é bem simples. Apesar de ter feito o código pedido, acabei fazendo errado, já que não coloquei
todos os dados coletados dentro do dicionário. Comparando os códigos não tem melhor ou pior, mas o meu não
seguiu o exigido. O unico ponto a ser destacado é a forma como ele fez o elif colocando uma condição antes
do item dicionário.
'''
# ============== MODELO CURSO EM VIDEO ===================================================================
aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-='*30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
