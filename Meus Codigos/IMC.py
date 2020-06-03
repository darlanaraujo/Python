print ('----------CALCULO DE IMC----------')
print ('')
nome = input ('Olá, para comerçarmos, qual o seu nome? ')
print ('Seja bem-vindo(a) {}, vamos começar!' .format(nome))
print()
peso = float (input ('Qual o seu peso? '))
altura = float (input ('Qual a sua altura? '))
s = peso / altura ** 2
print ('A soma do seu IMC é {}' .format (s))