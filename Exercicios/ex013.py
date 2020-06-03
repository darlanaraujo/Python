print ('{:=^40}'.format ('EXERCICIO 013'))
print ('Vamos calcular o aumento de \nsálario de um funcionário \nem 15% do valor atual')
n1 = float (input ('Qual o valor do sálario atual R$ '))
s = n1/100 * 115
s2 = s-n1
print ('O seu novo sálario é de R$ {:.2f} reais'.format (s))
print ('O valor do seu aumento corresponde a R$ {:.2f} reais'.format (s2))
print ('{:=^40}'.format ('='))