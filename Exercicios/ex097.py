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
'''def escreva(txt):
    print('-' * len(txt))
    print(f'{txt}')
    print('-' * len(txt))


txt = str(input('Escolha o titulo: '))
escreva(txt)'''
# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================
'''
No meu código ao usar a função len sem criar uma variável ficaria mais elegante uma vez que usei direto no print.
Porém ela não resolve a inclusão de mais 4 simbolos para deixar o texto centralizado. Só funciona se a pessoa digitar
o espaço ao criar o titulo. Por esse motivo o código do curso é mais funional.
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')