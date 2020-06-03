'''
DESAFIO 87

Aprimore o DESAFIO ANTERIOR, mostrando no final:

A) A SOMA de todos os VALORES PARES digitados.
B) A SOMA dos valores da TERCEIRA COLUNA.
C) O MAIOR valor da SEGUNDA LINHA.
'''
# ================= MODELO CRIADO =====================================================================================
'''linha = []
pares = 0

for c in range(0, 9):
    num = int(input(f'Digite o {c +1}º valor: '))
    linha.append(num)
    if num % 2 == 0:
        pares += num
soma = linha[2] + linha[5] + linha[8]
maior = max(linha[3:6])

print('='*30)
print(f'[{linha[0]:^5}][{linha[1]:^5}][{linha[2]:^5}]')
print(f'[{linha[3]:^5}][{linha[4]:^5}][{linha[5]:^5}]')
print(f'[{linha[6]:^5}][{linha[7]:^5}][{linha[8]:^5}]')

print('='*50)
print(f'A soma de todos os valores Pares: {pares}')
print(f'A soma da terceira coluna: {soma}')
print(f'O maior valor da segunda linha: {maior}')'''

# ================= MODELO APRIMORADO =================================================================================
lista = []

def cadastro():
    print('=' * 40)
    print(f'{"AULA 18 - EXERCÍCIO 87":^40}')
    print('=' * 40)

    for c in range(1, 10):
        lista.append(int(input(f'Digite o {c}º número: ')))
    print('=-'*20)
    menu()

def menu():
    print('='*40)
    print(f'{"ESCOLHA ABAIXO AS OPÇÕES":^40}')
    print('='*40)

    print('\033[33mA)\033[30m A SOMA DOS NÚMEROS PARES:')
    print('\033[33mB)\033[30m A SOMA DA TERCEIRA COLUNA')
    print('\033[33mC)\033[30m O MAIOR VALOR DA SEGUNDA LINHA')
    print('\033[33mD)\033[30m DIGITAR NOVOS NÚMEROS')
    print('\033[31mE)\033[30m SAIR DO PROGRAMA')
    print('=-'*20)
    loop()

def loop():
    menu = str(input('Escolha sua opção: ')).upper().strip()[0]
    print('=-' * 20)
    if menu == 'A':
        a()
    elif menu == 'B':
        b()
    elif menu == 'C':
        c()
    elif menu == 'D':
        lista.clear()
        cadastro()
    elif menu == 'E':
        print('FIM DO PROGRAMA')
    else:
        print('\033[30mATENÇÃO! \033[31mDados inválidos. Digite corretamente.\033[m')
        return loop()

def a():
    soma = 0
    for p, v in enumerate(lista):
        if v % 2 == 0:
            soma += v

    resultado()
    print(f'A soma dos valores pares são: {soma}')
    print('=-'*20)
    exit()

def b():
    soma = lista[2] + lista[5] + lista[8]
    resultado()
    print(f'A soma dos valores da terceira coluna são: {soma}')
    print('=-' * 20)
    exit()

def c():
    maior = max(lista[3:6])
    resultado()
    print(f'O maior número da segunda linha é: {maior}')
    print('=-' * 20)
    exit()

def resultado():
    print(f'[{lista[0]:^5}][{lista[1]:^5}][{lista[2]:^5}]')
    print(f'[{lista[3]:^5}][{lista[4]:^5}][{lista[5]:^5}]')
    print(f'[{lista[6]:^5}][{lista[7]:^5}][{lista[8]:^5}]')

def exit():
    while True:
        ex = str(input('Deseja continuar no programa? [S/N]: ')).upper().strip()[0]
        if ex == 'S':
            return menu()
        elif ex == 'N':
            print('FIM DO PROGRAMA')
            break
        else:
            print('\033[30mATENÇÃO! \033[31mDados inválidos. Digite corretamente.\033[m')
            return exit()

# INÍCIO DO PROGRAMA;
cadastro()

# ==================== ANÁLISE DO CÓDIGO ==============================================================================
'''
Novamente, meu código é mais simples e limpo. Porém nesse exercício que precisa fazer varredura da lista, em algumas
necessidades a função que ele deu para fazer um laço dentro da lista pode ter algumas vantagens em comparação ao meu
print que vai direto no item.

O meu código aprimorado sem dúvida é mais completo, no entando, não pode ser comparado uma vez que uso funções mais
avançadas.
'''
# ==================== MODELO CURSO EM VÍDEO ==========================================================================
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        #print('\033[33m', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
            #print('\033[m', end='')
    print()
print('=-'*20)
print(f'A soma dos valores pares são {spar}')

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da terceira coluna é {scol}')

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')'''


