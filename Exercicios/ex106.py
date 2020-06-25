'''
DESAFIO 106

Faça um MINI-SISTEMA que utilize o INTERACTIVE HELP do PYTHON. O usuário vai digitar o COMANDO e o MANUAL vai aparecer.
Quando o usuário digitar a palavra FIM, o programa se ENCERRARÁ.

Obs: Use CORES.
'''
# ============ CÓDIGO BASE ============================================================================================
def ajuda(txt):
    print('\033[47;30m~'*40)
    print(f'{"SISTEMA DE AJUDA PYTHON":^40}')
    print('~'*40)

    return txt

#Programa principal
a = ajuda('Função ou Biblíoteca >> ')
print(a)
# ============ CÓDIGO MELHORADO =======================================================================================

# ============ ANÁLISE DO CÓDIGO ======================================================================================

# ============ CÓDIGO DO CURSO EM VÍDEO ===============================================================================
