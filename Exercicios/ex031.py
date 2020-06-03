'''
DESAFIO 031

Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagem de até 200km
e R$ 0,45 para viagens mais longas.
'''

print('{:=^80}'.format('EXERCICIO 031'))
print()
print('{:#^161}'.format('#\n'))
print()
print('{:^80}'.format('SISTEMA - COBRANÇA DE PASSAGEM'))
print()
cit1 = str(input('Qual a cidade de origem? '.upper())).strip()
print()
cit2 = str(input('Qual a cidade de destino? '.upper())).strip()
print()
km = int(input('Qual a quilometragem entre as cidades? '))
print()
print('{:#^80}'.format(' INTINERÁRIO DA VIAGEM '))
print()
print('Cidade de origem e destino: {} X {}'.format(cit1, cit2).upper())
print()
print('Quilometragem percorrida: {} km'.format(km).upper())
#primeira opção de calculo
valor1 = km * 0.50
valor2 = km * 0.45
if km <= 200:
    print()
    print('Valor por Km rodado R$ 0,50 centavos'.format(km).upper())
    print()
    print('{:$^161}'.format('$\n'))
    print()
    print('Valor total a ser pago R$ {} reais'.format(valor1).upper())
else:
    print()
    print('Devido a quilometragem ser superior a 200km houve um desconto no valor!'.upper())
    print('Valor por Km rodado R$ 0,45 centavos'.format(km).upper())
    print()
    print('Valor total a ser pago R$ {} reais'.format(valor2).upper())
print()
print('{:#^161}'.format('#\n'))
print()
print('{:=^80}'.format(' FIM DO PROGRAMA '))