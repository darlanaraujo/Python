'''
DESAFIO 077

Crie um programa que tenha uma TUPLA com VÁRIAS PALAVRAS (sem acentos).
depois disso, você deve mostrar, para CADA PALAVRA, quais são as suas
VOGAIS.
'''
# ============= MODELO CRIADO ==============================================
'''
NÃO CONSEGUI CHEGAR A UMA CONCLUSÃO
'''

# ============= MODELO CURSO EM VÍDEO =====================================
'''lista = ('darlan', 'luana', 'davi', 'caroline', 'rodrigues')

for p in lista:
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos >>> ', end= '')
    for letra in p:
        if letra in 'aeiou':
            print(f'\033[33m{letra}\033[m', end= ' ')'''

# ============= MODELO COM MELHORIAS ======================================
lista = (str(input(f'Digite a 1º palavra: ')).lower(),
         str(input(f'Digite a 2º palavra: ')).lower(),
         str(input(f'Digite a 3º palavra: ')).lower(),
         str(input(f'Digite a 4º palavra: ')).lower(),
         str(input(f'Digite a 5º palavra: ')).lower())

for p in lista:
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos >>> ', end= '')
    for letra in p:
        if letra in 'aeiou':
            print(f'\033[33m{letra}\033[m', end= ' ')
