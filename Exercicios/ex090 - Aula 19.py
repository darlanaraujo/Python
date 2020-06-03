'''
DESAFIO 090 - AULA 19 DICIONÁRIOS

Faça um programa que leia NOME E MÉDIA de um aluno, quardando também a SITUAÇÃO
em um DICIONÁRIO. No final, mostre o conteúdo da estrutura na tela.
'''
# ============== MODELO CRIADO ===========================================================================
relatorio = {'aprovado': 'Aprovado', 'recuperação': 'Recuperação', 'reprovado': 'Reprovado'}

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
    print(f'Situação: {relatorio["aprovado"]}')
# ============== MELHORIA DO CÓDIGO ======================================================================

# ============== ANÁLISE DO CÓDIGO =======================================================================

# ============== MODELO CURSO EM VIDEO ===================================================================