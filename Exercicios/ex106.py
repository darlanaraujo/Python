'''
DESAFIO 106

Faça um MINI-SISTEMA que utilize o INTERACTIVE HELP do PYTHON. O usuário vai digitar o COMANDO e o MANUAL vai aparecer.
Quando o usuário digitar a palavra FIM, o programa se ENCERRARÁ.

Obs: Use CORES.
'''
# ============ CÓDIGO BASE ============================================================================================
'''def ajuda(txt):
    """
        --> A função recebe um parâmetro de texto que é usado para interação com o usuário. Não digitar a palavra que
        deseja saber o manual a função coloca essa palavra dentro da função help e devolve o conteúdo.
    :param txt: Mensagem que é usada para interação com o usuário
    :return: Mostra o manual das funções ou comando do Python.
    """
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
ajuda('Digite a Função ou Comando: >> ')'''
# ============ CÓDIGO MELHORADO =======================================================================================

# ============ ANÁLISE DO CÓDIGO ======================================================================================
'''
O meu código atende todos os requisitos no enunciado. Apesar de ter usando uma chamada de parâmetro desnecessária, pois
o texto poderia ter cido colocado dentro da função, ainda assim, o programa funciona. No entando o código do curso
ficou mais organizado e com definições mais bem definidas. A organização das cores utilizando uma lista e a criação de
uma função para criar um titulo personalizado, foram recursos muito bem pensados.
'''
# ============ CÓDIGO DO CURSO EM VÍDEO ===============================================================================
from time import sleep
c= ('\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m'        # 6 - branco
    )
def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com.upper()}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblíoteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
