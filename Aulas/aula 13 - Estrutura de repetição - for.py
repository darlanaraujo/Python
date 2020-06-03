'''
AULA 13 - ESTRUTURA DE REPETIÇÃO - FOR

EXTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE

Nessa aula vamos abordar os laços de repetição com a função 'for'.

Imagine um programa que precise fazer que um personagem saia da posição 0 e vá até a posição 10, chegando lá ele pega uma fruta e para.
Um comando simples, manualmente seria feito da seguinte forma;

paso, pula, paso, pula, pega, paso, pula, paso, pula, pega, paso, pula, pega, pare.

Com a função 'for' o comando ficaria da seguinte forma;

for variável in range(1, 10):
    if moeda:
        pega
    passo
    pula
pega
pare

'''

# =================== EXEMPLO DE COMANDOS ==================================================================

# Primeiro vamos ver o comando de repetição manual

'''print('passo')
print('pula')
print('pega')
print('passo')
print('pula')
print('passo')
print('pula')
print('pega')
print('passo')
print('pega')
print('pare!')


print('==============================================')'''

# Agora o mesmo comando usando um laço de repetição
for comando in range(0, 3):
    print('passo')
    print('pula')
    print('pega')
print('pare!')

'''
soma = 0
for c in range(0, 3):
    n1 = int(input('Digite um número: '))
    soma += n1
    #print(n1)
print('A soma dos valores digitados são: {}'.format(soma))
'''