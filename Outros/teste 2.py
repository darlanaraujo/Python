def teste(num):
    global a, b, c #Ao colocar essa função, as variáveis locais passaram ser globais
    a = 8
    b = num + 4 #NUM é o valor de A Global
    c = 2
    print(f'No programa Local, A vale {a}')
    print(f'No programa Local, B vale {b}')
    print(f'No programa local, C vale {c}')

print('PROGRAMA GLOBAL')
print('-' *30)
a = b = c = 0
a = 5
print(f'No programa Global, A vale {a}')
print(f'No programa Global, B vale {b}')
print(f'No programa Global, C vale {c}')

print()

print('PROGRAMA LOCAL')
print('-' *30)
teste(a) #O valor de A foi passado para o parâmetro NUM
print()
print('NA SEGUNDA CHAMADA OS RESULTADOS MUDAM')
print('=' *30)
print(f'No programa Global, A vale {a}')
print(f'No programa Global, B vale {b}')
print(f'No programa Global, C vale {c}')

print()

print('PROGRAMA LOCAL')
print('-' *30)
teste(a)




