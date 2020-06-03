'''
DESAFIO 037

Escreva um programa que LEIA UM NÚMERO INTEIRO.
E PEÇA para o usuário ESCOLHER qual será a BASE DE CONVERSÃO:

BINÁRIO
OCTAL
HEXADECIMAL
'''

# ===================== DEFINIÇÃO DO CABEÇALHO =================================================

print('\033[30m{}{}{}'.format('|', '='*40, '|'))
print('{}\033[33m{:^40}\033[30m{}'.format('|', 'BASE DE CONVERSÃO', '|'))
print('{}{}{}'.format('|', '='*40, '|'))


# ===================== INTERAÇÃO COMO USUÁRIO ================================================

numero = int(input('{}{}'.format('|', ' DIGITE UM NÚMERO: ')))
print('{}{}{}'.format('|', '-'*40, '|'))

# ===================== OPÇÕES DE ESCOLHA =====================================================

print('{}\033[33m{:^40}\033[30m{}'.format('|', 'ESCOLHA A FORMA DE CONVERSÃO', '|'))
print('{}{}{}'.format('|', '-'*40, '|'))
print('{}\033[32m{}{:<35}\033[30m{}'.format('|', ' [1] ', 'BINÁRIO:', '|'))
print('{}\033[34m{}{:<35}\033[30m{}'.format('|', ' [2] ', 'OCTAL:', '|'))
print('{}\033[35m{}{:<35}\033[30m{}'.format('|', ' [3] ', 'HEXADECIMAL:', '|'))
print('{}{}{}'.format('|', '-'*40, '|'))
formato = str(input('| CONVERTER PARA: ')).lower().strip()
print('{}{}{}'.format('|', '-'*40, '|'))

# ===================== FUNÇÕES DE CONVERSÃO =================================================

if '1' in formato or 'binário' in formato or 'binario' in formato:
    print('| \033[33m{} \033[30mCONVERTIDO PARA BINÁRIO \n| É IGUAL A: \033[33m{}'.format(numero, bin(numero)[2:]))
elif '2' in formato or 'octal' in formato:
    print('\033[30m| \033[33m{}\033[30m CONVERTIDO PARA OCTAL \n| É IGUAL A: \033[33m{}'.format(numero, oct(numero)[2:]))
elif '3' in formato or 'hexadecimal' in formato:
    print('\033[30m| \033[33m{}\033[30m CONVERTIDO PARA HEXADECIMAL \n| É IGUAL A: \033[33m{}'.format(numero, hex(numero)[2:]))
else:
    print('\033[31mATENÇÃO!\033[30m DIGITE UMA DAS OPÇÕES VÁLIDAS.')

# ==================== RODA PÉ DO PROGRAMA =====================================================

print('\033[30m{}{}{}'.format('|', '='*40, '|'))
print('{}\033[33m{:^40}\033[30m{}'.format('|', 'FIM DO PROGRAMA', '|'))
print('{}{}{}'.format('|', '='*40, '|'))