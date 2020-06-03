'''
DESAFIO 035

Desenvolva um programa que leia o comprimeito de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

print('{:=^80}'.format(' EXERCICIO 035 '))
print()
print('{:#^161}'.format('#\n'))
print()
print('{:^80}'.format('SISTEMA PARA FORMAÇÃO DE TRIÂNGULO'))
print()
print('ESSE SISTEMA COLETA DADOS DE 3 RETAS E INFORMA SE É POSSÍVEL A CONVERSÃO PARA UM TRIÂNGULO:')
print()
r1=float(input('INFORME O NÚMERO DA PRIMEIRA RETA: '))
print()
r2=float(input('informe o número da segunda reta: '.upper()))
print()
r3=float(input('informe o número da terceira reta: '.upper()))
print()
'''
if r1 == r2 and r1 == r3 and r2 == r3:
    formato = 'EQUILÁTERO'
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
    formato = 'ESÓSCELES'
elif r1 != r2 and r1 != r3 and r2 != r3:
    formato = 'ESCALENO'
'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um Triângulo!')
    print('E o seu formato é: {}'.format(formato))
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um Triângulo!')
    #print('E o seu formato é: {}'.format(formato))
print()
print('{:#^161}'.format('#\n'))
print()
print('{:=^80}'.format(' FIM DO PROGRAMA '))
