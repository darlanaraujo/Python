'''
DESAFIO 104

Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcioinar de forma semelhante à função INPUT() do Python, só que
fazendo a VALIDAÇÃO para aceitar apenas um valor numérico.

Ex: n=leiaint(''igite um número: ')
'''
# ============= CÓDIGO BASE ===========================================================================================
'''def leiaint(num):
    
        --> Função que funciona como o input, lendo uma informação iserida pelo usuário.
    :param num: Valor inserido pelo usuário.
    :return: Mostra o valor que o usuário digitou.
    
    while True:
        global n
        n = input(num)
        if n.isnumeric() == True:
            break
        else:
            print('\033[31mERRO! Digite apenas números.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''
# ============= CÓDIGO MELHORADO ======================================================================================

# ============= ANÁLISE DO CÓDIGO =====================================================================================
'''
Não consegui colocar o meu código para funcionar, minha linha de pensamento até estava correta, mas na hora de validar
o laço eu não soube faze-lo de forma correta. O código do curso ficou simples (mesmo sendo complexo) e detalhei ao
maximo cada função do código.
'''
# ============= CÓDIGO CURSO EM VÍDEO =================================================================================
def leiaint(msg): # A msg é o texto 'Digite um número'
    ok = False # Essa variável é apenas para iniciar ou parar o laço.
    valor = 0
    while True:
        n = str(input(msg)) # Aqui ele inseriu a mensagem na variavel n como se fosse n=str(input('Digite um número'))
        if n.isnumeric(): # Aqui ele vai verificar se n é um número.
            valor = int(n) # Sendo um número, n recebe o valor que foi digitado em n
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor # Sem esse retorno, o valor que foi inserido no laço não é validado.


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')