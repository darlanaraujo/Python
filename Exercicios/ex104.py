'''
DESAFIO 104

Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcioinar de forma semelhante à função INPUT() do Python, só que
fazendo a VALIDAÇÃO para aceitar apenas um valor numérico.

Ex: n=leiaint(''igite um número: ')
'''
# ============= CÓDIGO BASE ===========================================================================================
def leiaint(num):
    while True:
        global n
        n = input(num)
        if n.isnumeric() == True:
            break
        else:
            print('ERRO! Digite apenas números.')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
# ============= CÓDIGO MELHORADO ======================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================

# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
