'''
AULA 14 - Estrutura de repetição while

EXTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

EX:
Enquanto (while) não chegar a maçã (condição)
        passo (comando)
pega (fim da repetição)

while not maçã:
    passo
pega

Esse tipo de repetição (while) é mais versátil por permitir que se use um laço de repetição quando não se sabe
o numero de vezes necessário para interromper o laço. Já o laço for, você tem que definir a quantidade de repetições.

Ex:
while not maçã: # Essa é uma condição True. Quando ela se torma False o laço para.
    if chão == True:
        Passo
    if chão == False:
        Pula
    if moeda == True:
        Pega
pega


'''

# ====================== PRÁTICA DO COMANDO ============================================================

# Ex de um comando com for;

'''for c in range(1, 10):
    print(c)
print('Fim')'''

# Ex. do mesmo comando no while sabendo o limite de repetição, nesse caso sendo 10;

'''c = 1
while c < 10:
    print(c)
    c += 1 #Se não usar esse comando ele fica no laço infinito.
print('Fim')'''

# Ex. de uma repetição na qual não sei o limete de tentativas;

'''n = 1

while n != 0: #Ou seja, enquanto o numero digitado for diferente de 0 a repetição continua.
    n = int(input('Digite um número: '))
print('Fim')'''

# Ex. de um laço com confirmação do usuário. Ou seja, ele determina a continuidade do laço;

'''resposta = ''

while resposta != 'N':
    n = int(input('Digite um valor: '))
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()
print('Fim')'''

# Outro ex agora usando condições aninhadas;

n = 1
par = impar = 0 #Esse formato permite definir o mesmo resultado para duas variáveis diferentes.

while n != 0:
    n = int(input('Digite um número: '))
    if n != 0: #Ou seja, a condição só vai acontecer se o número digitado for diferente de 0, já que o 0 encerra a repetição.
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))