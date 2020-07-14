'''
DESAFIO 115

Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar pessoas pelo seu NOME e IDADE em um arquivo de texto
simples.

O sistema só vai ter 2 OPÇÕES: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas.
'''
# ============== CÓDIGO BASE ==========================================================================================
from modulos.cadastro import *
from modulos.cadastro.arquivo import *

'''inicio()'''
# ============== CÓDIGO MELHORADO =====================================================================================

# ============== ANÁLISE DO CÓDIGO ====================================================================================

# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sisitema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
