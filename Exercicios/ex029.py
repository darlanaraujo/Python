'''
Desafio 029

Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

print('{:=^80}'.format(' EXERCICIO 029 '))
print()
print('{:#^80} \n{:^80} \n{:#^80}'.format('#', 'SISTEMA DE CONTROLE DE TRANSITO', '#'))
print()
print('{:^80}'.format('Para iniciar o programa por favor identifique-se:').upper().strip())
print()
patente=str(input('Qual a sua patente? ')).upper().strip()
nome=str(input('Olá {}, por favor identifique seu nome e sobrenome: '.format(patente))).upper()
nome=nome.split()
print('{:#^80} \n{:^80} \n{:#^80}'.format('#', 'seja bem-vindo(a) ' + ' ' + patente + ' ' + nome[len(nome)-1], '#').upper())
print()
print('Primeiramente vamos saber qual a velocidade que o carro estava trafegando. \nE quais medidas tomaremos apos essa informação.'.upper())
print()
velocidade=int(input('Qual a velocidade (Km\h) do veiculo em questão? '.upper()))
if velocidade > 80:
    print()
    print('O veiculo estava trafegando acima da velicidade permitida.'.upper())
    print()
    condutor=str(input('Qual o nome do condutor? ').upper().strip())
    cnh=int(input('Qual o número da CNH? ').strip())
    carro=str(input('Qual o modelo do carro? ').upper().strip())
    ano=int(input('Qual o ano de fabricação? ').strip())
    velocidade=velocidade - 80
    multa=velocidade * 7.00
    print()
    print('{:#^161}'.format('#\n'))
    print()
    print('{:^80}'.format('DADOS DO VEICULO E CONDUTOR'))
    print()
    print('CONDUTOR: {} \nCNH: {} \nCARRO: {} \nANO DE FABRICAÇÃO: {}'.format(condutor, cnh, carro, ano))
    print()
    print('É cobrado o valor de R$ 7,00 reais por Km exedido a velocidade da via.'.upper())
    print()
    print('O veiculo estava {}Km acima da velocidade!'.format(velocidade).upper())
    print()
    print('O valor da multa é: {}'.format(multa).upper())
else:
    print()
    print('A velocidade do carro estava de acordo com a permitida para essa via. \nPode liberar o motorista.'.upper())
print()
print('{:#^161}'.format('#\n'))
print()
print('{:=^80}'.format(' FIM DO PROGRAMA '))
