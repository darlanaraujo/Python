#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex. 1834 - unidade 4 - Dezena 3 - Centena 8 - Milhar 1

'''
Esse exercicio, idetifiquei que por não usar ainda os recursos
de condicional, não foi possível fazer corretamente usando
string. O programa só da certo quando preenchido com 4 numéros.
Apenas usando a forma matemática deu certo independete da quantidade de caracteres
'''

print('{:=^40}'.format('EXERCICIO 23'))

numero=int(input('Digite um número entre 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analizando o número: {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#O formato abaixo só da certo quando digitado 4 numeros.


'''
numero=input('Digite um numero entre 0 a 9999: ')
dv=numero.split()
print('Unidade: {}'.format(dv[0][3]))
print('Dezena: {}'.format(dv[0][2]))
print('Centena: {}'.format(dv[0][1]))
print('Milhar {}'.format(dv[0][0]))
'''

'''
numero=input('Digite um número qualquer de 0 a 9999: ')
len(numero.split())
n0=(numero[0])
n1=(numero[1])
n2=(numero[2])
n3=(numero[3])
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))
'''