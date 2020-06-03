'''
DESAFIO 072

Crie um programa que tenha uma TUPLA totalmente
preenchida com uma contagem por EXTENSO, de ZERO até VINTE.

O programa deverá LER UM NÚMERO pelo teclado (ENTRE 0 E 20)
e mostrá-lo por EXTENSO.
'''

# ==================== MODELO CRIADO ==========================================================================
'''contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quadro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
            'Dezoito', 'Dezenove', 'Vinte')


while True:
    n1 = int(input('Digite um número de 0 a 20: '))

    for pos, cont in enumerate(contagem):
        if n1 == pos:
            print(f'Você digitou o número: \033[33m{cont}\033[m')
            break
    else:
        print('\033[31mNúmero invalido!\033[m')'''

# =================== MODELO CURSO EM VIDEO ===================================================================
'''lista = ('Zero', 'Um', 'Dois', 'Três', 'Quadro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
            'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente >>>', end= ' ')

print(f'Você digitou o número {lista[num]}')'''

# ================== MELHORIA DO PROGRAMA PARA UM LOOP INFINITO =================================================
lista = ('Zero', 'Um', 'Dois', 'Três', 'Quadro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
            'Dezoito', 'Dezenove', 'Vinte')

# ================ DEFINIÇÃO DE FUNÇÕES
def inicio():
    num = int(input('Digite um número de 0 a 20: '))
    if num > 20:
        print('Atenção! Dados inválidos, digite corretamente.')
        return inicio()
    else:
        print(f'Você digitou o número {lista[num]}')

    return pergunta()


def pergunta():
    while True:
        resp = str(input('Quer digitar outro número? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            return inicio()
        if resp == 'N':
            break
        else:
            print('Atenção! Dados inválidos, digite corretamente.')
            return pergunta()




# ================ INÍCIO DO PROGRAMA:
inicio()
print('Fim do programa')

