'''
DESAFIO 065

Crie um programa que LEIA VÁRIOS NÚMEROS inteiros pelo teclado.
No final da execução, mostre a MÉDIA ENTRE TODOS os valores e
e QUAL FOI O MAIOR E O MENOR valor lido.
O program deve PERGUNTAR AO USUÁRIO se ele QUER ou NÃO CONTINUAR
a DIGITAR VALORES.

A cada valor digitado o program pergunta se vai continuar.
'''

soma = contador = maior = menor = 0

resp = 'S'

while resp != 'N':
    n1 = int(input('Digite um número: '))
    soma += n1
    contador += 1

    if contador == 1:
        maior = menor = n1
    else:
        if n1 < menor:
            menor = n1
        if n1 > maior:
            maior = n1

    resp = str(input('Quer digitar outro número? [S/N]: ')).upper().strip()[0]
    #if resp == 'N':
        #start = resp
media = soma / contador
print('Você digitou {} números. E a média entre todos foi {:.2f}'.format(contador, media))
print('O MAIOR número digitado foi {}'.format(maior))
print('O MENOR número digitado foi {}'.format(menor))
