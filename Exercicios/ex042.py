'''
DESAFIO 042

Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:

-EQUILÁTERO: Todos os lados iguais.
-ESÓSCELES: Dois lados iguais.
-ESCALENO: Todos os lados diferentes
'''

print('{}{}{}'.format('|', '='*100, '|'))
print('{}{:^100}{}'.format('|', 'EXERCICIO 042', '|'))
print('{}{}{}'.format('|', '='*100, '|'))
print('INFORME O VALOR DE 3 RETAS, PARA SABER SE ELAS PODEM FORMAR UM TRIÂNGULO E QUAL O SEU FORMATO.')
print()
r1=float(input('INFORME O NÚMERO DA PRIMEIRA RETA: '))
print()
r2=float(input('informe o número da segunda reta: '.upper()))
print()
r3=float(input('informe o número da terceira reta: '.upper()))
print()
if r1 == r2 == r3: #r1 == r2 and r1 == r3 and r2 == r3:
    formato = 'EQUILÁTERO'
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
    formato = 'ESÓSCELES'
elif r1 != r2 != r3 != r1: #r1 != r2 and r1 != r3 and r2 != r3:
    formato = 'ESCALENO'

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