'''
DESAFIO 081

Crie um programa que vai LER VÁRIOS Nº e colocar em uma LISTA.

Deposi disso, mostre:
A) QUANTOS Nº foram digitados.
B) A lista de valores, ordenada de forma DECRESCENTE.
C) Se o valor 5 foi digitado e ESTÁ ou NÃO na LISTA.
'''

# ================= MODELO CRIADO ====================================================
valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    print('Número cadastrado com sucesso!')
    print('-='*15)

    resp = str(input('Deseja cadastrar outro? [S/N]: ')).upper().strip()[0]
    if resp in 'nN':
        break

print(f'A) Você cadastrou {len(valores)} números.')
valores.sort(reverse=True)
print(f'B) Segue a lista de valores na ordem decrescente: {valores}')
if 5 in valores:
    print(f'C) O número 5 ESTÁ na lista, com {valores.count(5)} unidades.')
else:
    print(f'C) O número 5 NÃO está na lista.')

# =============== MODELO CURSO EM VIDEO ==============================================
'''O CÓDIGO FOI O MESMO!'''