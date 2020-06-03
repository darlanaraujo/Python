'''
EXERCICIO 036

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em
QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do
salário ou então o empréstimo será negado.
'''

print('#'*150)
print('#'*150)
print('{:^150}'.format('\033[1;33mSISTEMA DE EMPRESTIMO BANCÁRIO\033[m'))
print('='*150)
print('{:^150}'.format('\033[4;32mINFORMAÇÕES DO CLIENTE\033[m'))
print()
nome = str(input('INFORME O NOME DO CLIENTE: ')).upper().strip()
cpf = int(input('INFORME O CPF: '))
salario = float(input('INFORME A RENDA MENSAL: R$ '))
print()
print('='*150)
print('='*150)
print('{:^150}'.format('\033[1;4;33mDADOS DO IMÓVEL\033[m'))
print()
imovel = float(input('INFORME O VALOR DO IMÓVEL: R$ '))
tempo = int(input('INFORME A QUANTIDADE DE PARCELAS: '))
print()
print('#'*150)
print('#'*150)
print('{:^150}'.format('\033[1;33mDADOS DO CADASTRO\033[m'))
print()
print('\033[1;4;30mCLIENTE:\033[m \033[1;32m{}\033[m'.format(nome))
print('\033[1;4;30mCPF:\033[m \033[1;33m{}\033[m'.format(cpf))
print('\033[1;4;30mRENDA MENSAL:\033[m \033[1;32mR$ {:.2f} REAIS\033[m'.format(salario))
print('\033[1;4;30mVALOR DO IMÓVEL:\033[m \033[1;33mR$ {:.2f} MIL REAIS\033[m'.format(imovel))
print('\033[1;4;30mQUANTIDADE DE PARCELAS:\033[m \033[1;33m{} MESES\033[m'.format(tempo))
print()
ok = str(input('DESEJA FAZER A COTAÇÃO (S/N)? ').lower()).strip()
print()
if ok == 's' or ok == 'sim':
    print('#'*150)
    print('#'*150)
    print('{:^150}'.format('\033[1;33mDADOS DO FINANCIAMENTO\033[m'))
    print()
    soma = imovel / tempo
    renda = salario * 30 / 100
    if soma <= renda:
        print('{: ^150}'.format('\033[30m$\033[m'*70))
        print('{:^150}'.format('\033[1;4;33mCADASTRO APROVADO\033[m'))
        print('{: ^150}'.format('\033[30m$\033[m'*70))
        print()
        print('\033[1;30mO VALOR DA MENSALIDADE É DE\033[m \033[1;4;33mR$ {:.2f} REAIS\033[m'.format(soma))
    else:
        print('{: ^150}'.format('\033[30m$\033[m'* 70))
        print('{:^150}'.format('\033[1;4;31mCADASTRO NEGADO!\033[m'))
        print('{: ^150}'.format('\033[30m$\033[m'* 70))
        print()
        print('\033[1;30mO VALOR DA MENSALIDADE É DE\033[m \033[1;4;33mR$ {:.2f} REAIS\033[m'.format(soma))
        print('\033[1;4;31m*INFELIZMENTE O FINANCIAMENTO É SUPERIOR A 30% DA SUA RENDA MENSAL!\033[m')

print()
print('='*150)
print('{:^150}'.format(' \033[1;30mFIM DO PROGRAMA!\033[m '))
print('#'*150)
print('#'*150)

