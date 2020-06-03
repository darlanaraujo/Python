#Faça um programa que leia a largura e altura de uma parede em
#metros quadrados, calcule a sua área e a quantidade de tinte necessáira
#para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
print('{:=^40}'.format('EXERCICIO 011'))
print('Um litro de tinta da para pintar 2m² \nQuantos litros são necessários para esse serviço?')
n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))
s = n1*n2
s1 = s/2
print ('A sua parede tem {} m² \nDessa forma será necessário {} litros \nde tinta para esse serviço!'.format (s, s1))
print ('{:=^40}'.format ('='))