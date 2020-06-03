'''
DESAFIO 078

Faça um progrma que LEIA 5 VALORES Nº e guarde-os em uma LISTA.

No final mostre qual foi o MAIOR e o MENOR valor digitado e as
suas respectivas POSIÇÕES na lista.
'''

# ================ MODELO CRIADO =====================================
valores = []

for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}º número: ')))
print('='*40)
print(f'Lista dos valores digitados: {valores}')
print(f'O maior número digitado foi {max(valores)}, nas posições: ', end= '')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p +1}...', end= ' ')
print()
print(f'O menor número digitado foi {min(valores)}, nas posições: ', end= '')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p +1}...', end= ' ')
print()


# ================= MODELO CURSO EM VIDEO ===============================
'''listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} na posição: ', end= '')
for p, v in enumerate(listanum):
    if v == maior:
        print(f'{p}...', end= ' ')
print()
print(f'O menor valor digitado foi {menor} na posição: ', end= '')
for p, v, in enumerate(listanum):
    if v == menor:
        print(f'{p}...', end= ' ')
print()'''
