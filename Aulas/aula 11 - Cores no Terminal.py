'''
AULA 11 - CORES NO TERMINAL
Como colocar cores nos textos do programa.

Padrão ANSI - escape sequence

exemplo: (\033[style+text+back+m
\033[0;33;44m

style:
0 = nome ou nada
1 = bold ou negrito
4 = underline ou _
7 = negativo ou inverte a ordem da cor
------------------------------------------------
text:                   back: (fundo)
30 = branco             40 = branco
31 = vermelho           41 = vermelho
32 = verde              42 = verde
33 = amarelo            43 = amarelo
34 = azul               44 = azul
35 = roxo               45 = roxo
36 = azul bebe          46 = azul bebe
37 = cinza              47 = cinza

'''

'''
#Nos exemplos abaixo o fundo vai até o final do programa.
print('\033[0;30;41m Teste') #Styl comum + Text branco + Back vermelho
print('\033[4;33;44m Teste') #Styl underline + Text amarelo + Back azul
print('\033[0;1;35;43m Teste') #Styl - underline + negrito + Text roxo + Back amarelo
print('\033[30;42m Teste') #Styl comum + Text branco + Back verde
print('\033[m Teste') #Styl comum + Text cinza + Back preto (invertido)
print('\033[7;30m Teste') #Styl negativo + Text branco + Back (invertido)
print('\033[m')
'''

'''
#Abaixo um print do fundo apenas cobrindo o texto.

print('\033[7;30m Darlan Araujo \033[m')
print('\033[30m Darlan Araujo \033[m')
print()
n1 = 100
n2 = 350
soma = n1 + n2
print('A soma dos valores de \033[31m{}\033[m mais \033[33m{}\033[m é igual a \033[32m{}\033[m!!'.format(n1, n2, soma))
'''

#Uma outra opção de trabalhar com cores é fazendo variaveis.

cores = {'limpa':'\033[m',
         'branco': '\033[30m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'p&b':'\033[7;30m'}

nome = 'Darlan Araujo'
print('Olá {}{}{}, prazer em te conhecer!'.format(cores['vermelho'], nome, cores['limpa']))