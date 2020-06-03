print ('{:=^40}'.format ('EXERCICIO 006'))
print ('Vamos ver alguns calculos?')
n1 = int (input ('Dígite um número: '))
do = n1*2
tr = n1*3
rz = n1 ** (1/2)
print ('O dobro de {} é {}'. format (n1, do))
print ('O triplo de {} é {}'.format (n1, tr))
print ('A raiz quandrada de {} é {}'.format (n1, rz))
#a linha de baixo foi usado a função de quebra de linha utilizando \n
print ('O dobro de {} é: {} \nO triplo de {} é: {} \nA raiz quadrada de {} é: {}'.format (n1,do, n1, tr, n1, rz))
print ('{:=^40}'.format ('='))