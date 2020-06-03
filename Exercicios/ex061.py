'''
DESAFIO 061

Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO E A RAZÃO DE UMA PA
mostrando os 10 PRIMEIROS TERMOS da progressão usando a estrutura while.

'''

termo = int(input('Digite o TERMO: '))
razao = int(input('Digite a RAZÃO: '))

contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end= '')
    termo += razao
    contador += 1
print('FIM')