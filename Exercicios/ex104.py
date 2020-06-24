'''
DESAFIO 104

Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcioinar de forma semelhante à função INPUT() do Python, só que
fazendo a VALIDAÇÃO para aceitar apenas um valor numérico.

Ex: n=leiaint(''igite um número: ')
'''
# ============= CÓDIGO BASE ===========================================================================================
def leiaint(num):
    '''
        --> Função que funciona como o input, lendo uma informação iserida pelo usuário.
    :param num: Valor inserido pelo usuário.
    :return: Mostra o valor que o usuário digitou.
    '''
    while True:
        global n
        n = input(num)
        if n.isnumeric() == True:
            break
        else:
            print('\033[31mERRO! Digite apenas números.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
# ============= CÓDIGO MELHORADO ======================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================

# ============= CÓDIGO CURSO EM VÍDEO =================================================================================


