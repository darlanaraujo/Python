'''
DESAFIO 099

Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS
com valores inteiros.

Seu programa tem que ANALISAR todos os VALORES e dizer qual deles É O MAIOR.
'''
# ================= MODELO CRIADO =====================================================================================
from time import sleep

def maior(* num):
    print('Analisando os valores: ', end='')
    for valor in num:
        print(valor, end=' ')
        sleep(.5)
    print()
    print(f'{len(num)} números foram informado. O maior valor é {max(num)}')
    print('-=' *20)
    sleep(1.5)


maior(1, 8, 3, 5, 18, 2)
maior(23, 12, 66, 4)
maior(2, 1, 9)
maior(0, 0, 0, 0)
maior(6)
# ================= MELHORIA DO CÓDIGO ================================================================================
'''from time import sleep
num = []
def maior(* num):
    print('Analisando os valores: ', end='')
    for valor in num:
        print(valor, end=' ')
        sleep(.5)
    print()
    print(f'{len(num)} números foram informado. O maior valor é {max(num)}')

while True:
    num.append(int(input('Digite um valor: ')))
    print('='*40)
    resp = str(input('Deseja adicionar outro? [S/N]: '))
    if resp in 'nN':
        break
print('='*40)
maior(* num)'''
# ================= ANAÁLISE DO CÓDIGO ================================================================================
'''
Ao utilizar as funções len e max no meu código eu consigo executar a tarefa sem a necessidade de fazer 2 variáveis além
de não precisar usar o if ou else para isso. Se os parâmetros forem preenchidos meu código ficou melhor. A unica falha
é no caso do parâmetro ficar vazio. Que no meu código daria erro, pois a função max e len não teria dados para ler.
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
'''from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True) #Essa função flush=True era para um erro ao executar o sleep
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''