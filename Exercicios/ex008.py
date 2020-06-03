#Escreva um programa que leia um valor em metros e o exiba
#convertido em centímetros e milimetros
print('{:=^40}'.format('EXERCICIO 008'))
print('Vamos aprender a conversão de medidas!')
m = float(input('Dígite uma valor em metros: '))
ce = m*100
mm = m*1000
print('{} corresponde há {:.0f} centimetros e há {:.0f} milimetros'.format(m, ce, mm))
print('{:=^40}'.format('='))
