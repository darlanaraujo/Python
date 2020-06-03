'''
DESAFIO 080

Crie um programa aonde o usuário possa digitar 5 VALORES Nº e
cadastre-os em uma LISTA, JA NA POSIÇÃO CORRETA de inserção
(sem usar o sort().

No final, mostre a LISTA ORDENADA na tela.
'''

# ============ MODELO CRIADO =====================================================
'''valores = []

for c in range(1, 6):
    n1 = int(input(f'Informe o {c}º número: '))
    if c == 1:
        valores.append(n1)
        print(f'O valor {n1} foi adicionado no início da lista')
    elif n1 > max(valores):
        valores.insert(len(valores), n1)
        print(f'O valor {n1} foi adicionado no final da lista')

    elif n1 > min(valores) and n1 < max(valores):
        if c == 3:
            valores.insert(1, n1)
        else:
            if n1 < valores[1]:
                valores.insert(1, n1)
            if n1 > valores[1] and n1 < valores[2]:
                valores.insert(2, n1)
            if n1 > valores[2]:
                valores.insert(-1, n1)
        print(f'O valor {n1} foi adicionado no meio da lista')

    else:
        valores.insert(0, n1)
        print(f'O valor {n1} foi adicionado no início da lista')


print(f'Segue a ordem dos numeros adicionados a lista: {valores}')'''

# ============= MODELO CURSO EM VIDEO =============================================

lista = list()

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > max(lista): #n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-'*20)
print(f'Os valores digitados em ordem foram {lista}')
