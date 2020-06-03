'''
DESAFIO 049

Refaça o DESAFIO 009 mostrando a TABUADA de um número que o usuário escolher,
só que agora utilizando um LAÇO for.
'''

n1 = int(input('Escolha o número que deseja multiplicar: '))
print('='*60)
print()
print('A TABUADA DE {} É:'.format(n1))
print()
print('|'+'='*17+'|')
for tabuada in range(1, 10+1):
    soma = n1 * tabuada
    print('| {:3} X {:3} = {:3} |'.format(n1, tabuada, soma))
print('|'+'='*17+'|')
for tabuada2 in range(10+1, 20+1):
    soma2 = n1 * tabuada2
    print('| {:3} X {:3} = {:3} |'.format(n1, tabuada2, soma2))
print('|'+'='*17+'|')