#Faça um programa que leia uma frase e mostre:
#Quantas veses aparece a letra "a".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

print('{:=^40}'.format('EXERCICIO 026'))
print(' ')
frase=str(input('Digite uma frase: ')).strip()
frase=frase.lower().replace('ã','a') #Esse comando eu mudeia a variável com a função lower que colocou tudo minusculo, e com a função replace que trocou um caractere por outro.
print('A letra "a" aparece: {} vezes'.format(frase.count('a'))) #Comando que conta a quantidade do caractere selecionado.
print('A letra "a" aparece a primeira vez na posição: {}'.format(frase.find('a')+1)) #Comando que mostra aonde o caractere apareceu a primeira vez
print('A letra "a" aparece a última vez na posição: {}'.format(frase.rfind('a')+1-frase.count(' '))) #Comando que mostra aonde o caractere apareceu por último
print('')
print('{:=^40}'.format('='))