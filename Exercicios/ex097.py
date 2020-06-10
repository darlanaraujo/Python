'''
DESAFIO 097

Faça um programa que tenha um FUNÇÃO chamada ESCREVA(), que receba um texto qualquer como
PARÂMETRO e mostre uma mensagem com tamanho adaptável.

Ex: escreva('Olá, Mundo!')
Saída:
---------------
  Olá, Mundo!
---------------
'''
# ================= MODELO CRIADO =====================================================================================
def escreva(txt):
    print('-' * len(txt))
    print(f'{txt}')
    print('-' * len(txt))

txt = str(input('Escolha o titulo: '))

escreva(txt)

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
