'''
DESAFIO 085

Crie um programa aonde o usuário possa digitar SETE VALORES Nº e
CADASTRE-OS em uma LISTA ÚNICA que mantenha separados os valores
PARES e ÍMPARES. No final, mostre os valores PARES E ÍMPARES em
ordem CRESCENTE.
'''
# =================== MODELO CRIADO ===================================================================================
lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print('='*60)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')

# ================== ANÁLISE DOS CÓDIGOS ==============================================================================
'''
Ao meu ver, meu código ficou mais organizado, uma vez que não foi necessário declarar a váriável valor 2x.
e a forma do print, eu jpa defini a ordem dos números dentro do print, economizando 2 linhas de código. Ainda usei
uma forma diferente da função variavel.sort() / sorted(variavel)
'''
# ================== MODELO CURSO EM VIDEO ============================================================================
'''núm = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram {núm[0]}')
print(f'Os valores ímpares digitados foram {núm[1]}')'''
