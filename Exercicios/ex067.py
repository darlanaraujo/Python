'''
DESAFIO 067

Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez,
para cada valor digitado pelo usuário. O programa será INTERROMPIDO quando
o número solicitado for NEGATIVO.
'''
print('-='*15)
print(f'{"PROGRAMA DE TABUADA":^30}')
print('=-'*15)
#n1 = int(input('Digite um número: '))
while True:
    n1 = int(input('Digite um número: '))
    print('|'+'-'*15+'|')

    #Função para parar o programa quando digitar zero ou menos valor
    if n1 < 0:
        break

    for c in range(1, 11):
        soma = n1 * c
        print('|'+f'{n1:2} x {c:2} = {soma:4}'+'|')
    print('|' + '-' * 15 + '|')
    while True:
        resp = str(input('Deseja ver outra tabuada? [S/N]: '))
        if resp == 's':
            break
        elif resp == 'n':
            break
        else:
            print('Informação invalida!')
    if resp == 'n':
        break

print('Fim do programa')
