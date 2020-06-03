'''
DESAFIO 038

Escreva um programa que LEIA DOIS NÚMEROS INTEIROS e COMPARE-OS, mostrando
na tela uma MENSAGEM:

Qual é o MAIOR número. O PRIMEIRO ou SEGUNDO ou NÃO EXISTE MAIOR os dois são iguais.
'''

print('#'*180)
print('#'*180)
print('{:^180}'.format('EXERCICIO 038'))
print()
print('VOU PEDIR QUE DIGITE 2 NÚMEROS A SUA ESCOLHA. E VOU TE DIZER QUAL O MAIOR ENTRE ELES.')
print()
n1 = int(input('ME DIGA UM NÚMERO: '))
print('='*70)
n2 = int(input('ME DIGA OUTRO NÚMERO: '))
print()
if n1 < n2:
    print('MUITO FACIL! O SEGUNDO NÚMERO É MAIOR QUE O PRIMEIRO.')
elif n1 > n2:
    print('O PRIMEIRO NÚMERO É MAIOR QUE O SEGUNDO!')
else:
    print('OHOU! OS DOIS NÚMEROS SÃO IGUAIS!')
print('='*180)
print('{:^180}'.format('FIM DO PROGRAMA!'))
print('#'*180)
print('#'*180)