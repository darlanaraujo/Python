'''
DESAFIO 034

Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.
'''

print('{:=^80}'.format(' EXERCICIO 034 '))
print()
print('{:#^161}'.format('#\n'))
print()
print('{:^80}'.format('SISTEMA DE AJUSTE SALARIAL'))
print()
print('OS AJUSTES SALARIAIS SERÃO DIVIDIDOS DA SEGUINTE FORMA: \nSALÁRIOS IGUAIS OU ABAIXO DE R$ 1.250,00 REAIS RECEBERAM 15% A MAIS. \nSALÁRIOS SUPERIORES A ESSE VALOR RECEBERAM 10% A MAIS.')
print()
nome=str(input('QUAL O NOME COMPLETO DO FUNCIONÁRIO? ')).upper().strip()
print()
salario=float(input('QUAL SALÁRIO ATUAL? '))
if salario <= 1250:
    reajuste = salario * (15) / 100
else:
    reajuste = salario * (10) / 100
print()
print('{:=^161}'.format('=\n'))
print()
soma = reajuste + salario
print('DADAS AS PROPORÇÕES PRÉ-DEFINIDAS DOS REAJUSTE SALARIAL:')
print()
print('O FUNCIOÁRIO {} RECEBIA R$ {:.2f} REAIS. O VALOR DO REAJUSTE FOI R$ {:.2f}'.format(nome, salario, reajuste))
print()
print('{:$^161}'.format('$\n'))
print()
print('Parabéns {} segue abaixo seu novo salário'.format(nome).upper())
print()
print('VALOR TOTAL DO SALÁRIO REAJUSTADO R$ {:.2f}'.format(soma))
print()
print('{:=^80}'.format(' FIM DO PROGRAMA '))
