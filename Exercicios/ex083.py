'''
DESAFIO 083

Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use
PARÊNTESES. Seu aplicativo deverá analisar se a EXPRESSÃO está com os
PARÊNTESES ABERTOS E FECHADOS na ORDEM CORRETA.
'''
# ================= MODELO CRIADO ===================================================================================
'''formula = ''

print('='*50)
print(f'{"EXPRESSÃO MATEMÁTICA":^50}')
print('='*50)
print('\033[33m>>> Crie uma FORMULA utilizando (parênteses)\033[m')
#formula += str(input('Digite uma formula: '))
formula += str(input('Digite uma formula: '))

formula.split()

if formula.count('(') == formula.count(')'):
    print(f'\033[33mA formula {formula} é válida.')
else:
    print(f'\033[31mA formula {formula} não é valida. Verifique a falta de PARÊNTESES')'''


'''O CÓDIGO SÓ DA CERTO COM VARIÁVEL SIMPLES. A FUNÇÃO .split() NÃO FUNCIONA COM VARIÁVEL COMPOSTA.'''

# ================== MODELO CURSO EM VIDEO =========================================================================
pilha= []

expr = str(input('Digite a expressão: '))
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('Sua expressão está valida.')
else:
    print('Sua expressão está errada!')