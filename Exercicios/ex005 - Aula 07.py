print ('{:=^40}'.format ('EXERCICIO 005'))
print ('Vamos descobrir qual o seu antecessor, e seu sucessor!')
n1 = int (input ('Dígite um número: '))
an = n1 - 1
su = n1 + 1
print ('O antecessor de {} é {} e o sucessor é {}'. format (n1, an, su))
#Esse código poderia ser feito de outra forma. Para isso seria ncessário apagar as variáveis (an) e (su)
#print ('o antecessor de {} é {} e o sucessor é {}'.format (n1, (n1-1), (n1+1)))
#Quando não precisa guarda a variável, pode fazer as somas usando () dentro dos .format
print ('{:=^40}'.format ('='))
