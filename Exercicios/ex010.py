#Crie um programa que converta o valor de reais em dolares
print('{:=^40}'.format('EXERCICIO 010'))
print('Conversão de Real X Dolar')
n1 = float(input('Qual o seu valor em Reais? R$ '))
s = n1/4.86
print('Com a cotação do momento, com R$ {:.2f} reais \nDa para comprar U$ {:.2f} dolares'.format(n1, s))
print('{:=^40}'.format('='))