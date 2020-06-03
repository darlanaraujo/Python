'''
AULA 15 - INTERROMPENDO REPETIÇÕES WHILE

LAÇOS DE REPETIÇÃO PARTE 3

Nessa aula vamos aprender a usar o laço com uma função TRUE que da uma comando infinito para o laço.
Ao invés de usar uma condição. E para fazer com que o laço pare em algum momento, usamos a função BREAK.

Ex: Estrutura com uma condição.
    while not maçã:
        print(passo)
    print(pega)

Ex: Estrutura sem uma condição.
    while True:
        if == chão:
            print(passo)
        if == vazio:
            print(pula)
        if == moeda:
            print(pega)
        if == trofeu:
            print(pega)
            break
    print(fim)

Nesse caso, dentro do laço de repetição o objetivo foi alcançado ao chegar no trofeu, e somente quando isso ocorreu
o programa para o laço.

'''

# ============== EXEMPLOS =========================================================================

# Exemplo com uma condição:

'''sexo = ''# <- Condição

nome = str(input('Nome do cliente: ')).upper()
sexo = str(input('Sexo [M/F]: ')).upper().strip()[0] # <- Variável

while sexo != 'MASCULINO': # <- Condição do laço
    print('Dados invalidos! Digite corretamente.')
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0] # <- Repetição da variável
    if sexo == 'M':
        sexo = 'MASCULINO'

idade = int(input('Idade: '))
print('='*15)
print('Nome: {}, Sexo: {}, Idade: {} anos'.format(nome, sexo, idade))'''

# Exemplo sem a condição

'''nome = str(input('Nome do cliente: ')).upper()
while True:
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        sexo = 'MASCULINO'
        break
    print('Dados invalidos! Digite corretamente.')

idade = int(input('Idade: '))
print('='*15)
#print('Nome: {}, Sexo: {}, Idade: {} anos'.format(nome, sexo, idade))
print(f'Nome: {nome}, Sexo: {sexo}, Idade: {idade} anos.')'''

#=================================================================================

