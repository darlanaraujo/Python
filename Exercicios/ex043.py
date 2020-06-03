'''
DESAFIO 043

Desenvolva uma lógica que LEIA O PESO e a ALTURA DE UMA PESSOA.
CALCULE SEU IMC e mostre seu status, de acordo com a tabela abaixo:

ABAIXO DE 18.5: ABAIXO DO PESO.
ENTRE 18.5 E 25: PESO IDEAL.
DE 25 ATÉ 30: SOBREPESO.
DE 30 ATÉ 40: OBESIDADE.
ACIMA DE 40: OBESIDADE MÓRBIDA
'''

#Definição de cores para o programa

b = '\033[30m'
a = '\033[33m'
v = '\033[31m'
vd = '\033[32m'
l = '\033[m'

print('{}{}{}{}'.format(b, '|', '='*100, '|'))
print('{}{}{:^100}{}{}'.format('|', a, 'CALCULO DO IMC', b, '|'))
print('{}{}{}'.format('|', '='*100, '|'))
print('{}{:^100}{}'.format('|', 'CALCULE O SEU ÍNDICE DE MASSA CORPORAL', '|'))
peso = float(input('{}{}{}{}'.format('|', a, 'INFORME O SEU PESO: ', b)))
altura = float(input('{}{}{}{}'.format('|', a, 'INFORME A SUA ALTURA: ', b)))
if '.' in altura:

print('{}{}{}'.format('|', '='*100, '|'))
print('{}{}{:^100}{}{}'.format('|', a, 'RESULTADO DO IMC', b, '|'))
print('| COM BASE NOS DADOS INFORMADOS: \n| \n| O SEU PESO É: {}{}{} Kg \n{}| E A SUA ALTURA É: {}{}{} cm'.format(a, peso, b, b, a, altura, b))
imc = peso / altura ** 2
print('|')
if imc < 18.5:
    print('| {}CUIDADO!{} O seu IMC é: {}{:.2f}{}. Você está {}ABAIXO DO PESO{}.'.format(v, b, a, imc, b, v, b))
elif imc == 18.5 or imc < 25:
    print('| {}PARABÉNS!{} O seu IMC é: {}{:.2f}{}. Você está no {}PESO IDEAL{}.'.format(vd, b, a, imc, b, vd, b, vd, b))
elif imc == 25 or imc < 30:
    print('| {}ATENÇÃO!{} O seu IMC é: {}{:.2f}{}. Você está com {}SOBREPESO{}.'.format(a, b, a, imc, b, a, b))
elif imc == 30 or imc < 40:
    print('| {}CUIDADO!{} O seu IMC é: {}{:.2f}{}. Você está no nível de {}OBESIDADE{}.'.format(v, b, a, imc, b, v, b))
else:
    print('| {}ATENÇÃO MÁXIMA!{} O seu IMC é: {}{:.2f}{}. Você está no nível de {}OBESIDADE MÓRBIDA{}. {}Procure ajuda o quanto antes!{}'.format(v, b, a, imc, b, v, b, a, b))
print('{}{}{}'.format('|', '='*100, '|'))
print('{}{}{:^100}{}{}'.format('|', a, 'FIM DO PROGRAMA', b, '|'))
print('{}{}{}'.format('|', '='*100, '|'))