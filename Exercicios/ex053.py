'''
DESAFIO 053

Crie um programa que leia uma FRASE qualquer e diga se ela é
um PALINDROMO, DESCONSIDERANDO OS ESPAÇOS.

**PALINDROMO É UMA PALAVRA QUE PODE SER LIDA DE TRAZ PARA FRENTE OU AO CONTRÁRIO.

EX: APOS A SOPA - A SACADA DA CASA - A TORRE DA DERROTA - O LOBO AMA O BOLO - ANOTARAM A DATA DA MARATONA
'''

'''frase = str(input('DIGITE UMA FRASE: ')).upper().strip().split()
junto = ''.join(frase)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print('O INVERSO DE {} É {}'.format(junto, inverso))
if inverso == junto:
    print('TEMO UM PALINDROMO!')
else:
    print('NÃO TEMOS UM PALINDROMO!')'''

# ================= OUTRA FORMA DE FAZER O PROGRAMA ===========================================================

frase = str(input('DIGITE UMA FRASE: ')).upper().strip().split()
junto = ''.join(frase)
#Essa função de fatiamento substituiu a necessidade do laço.
inverso = junto[::-1] # não colocar nada antes e depois dos : informa que não define de onde começa a ler. O -1 mostra que é de traz para frente.
print('O INVERSO DE {} É {}'.format(junto, inverso))
if inverso == junto:
    print('TEMO UM PALINDROMO!')
else:
    print('NÃO TEMOS UM PALINDROMO!')
