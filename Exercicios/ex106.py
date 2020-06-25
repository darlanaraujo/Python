'''
DESAFIO 106

Faça um MINI-SISTEMA que utilize o INTERACTIVE HELP do PYTHON. O usuário vai digitar o COMANDO e o MANUAL vai aparecer.
Quando o usuário digitar a palavra FIM, o programa se ENCERRARÁ.

Obs: Use CORES.
'''
# ============ CÓDIGO BASE ============================================================================================
def ajuda(txt):
    from time import sleep
    while True:
        print('\033[44;30m~'*40)
        print(f'{"SISTEMA DE AJUDA PYTHON":^40}')
        print('~'*40)

        palavra = str(input(f'\n\033[m{txt}').lower())

        if palavra == 'fim':
            sleep(.5)
            print('\033[41;30m~'*12)
            print(f'{"ATÉ LOGO!":^12}')
            print('~'*12)
            break

        print('\033[47;30m~'*50)
        print(f'{"ACESSANDO O MANUAL DO COMANDO " +palavra.upper():^50}')
        print('~'*50)
        print('\033[m')
        sleep(.5)

        print('\033[7;30m')
        help(palavra)
        print('\033[m')
        sleep(2)


#Programa principal
ajuda('Digite a Função ou Comando: >> ')
# ============ CÓDIGO MELHORADO =======================================================================================

# ============ ANÁLISE DO CÓDIGO ======================================================================================

# ============ CÓDIGO DO CURSO EM VÍDEO ===============================================================================
