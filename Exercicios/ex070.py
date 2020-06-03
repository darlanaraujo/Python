'''
DESAFIO 070

Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS.
O programa deverá PERGUNTAR se o USUÁRIO vai continuar.
No final mostre:

A) Qual é o TOTAL GASTO na compra.
B) Quantos produtos CUSTAM MAIS de R$ 1.000.
C) Qual é o NOME do produto MAIS BARATO.
'''
# ============== VARIAVEIS GLOBAIS =================================================================
total = mais = menos = cont = 0
nome = ''

# ============== INÍCIO DO PROGRAMA - CABEÇALHO ====================================================
print(f'\033[30m|{"-"*50}|')
print(f'|{"$"*50}|')
print(f'|{"$"*50}|')
print(f'|\033[33m{"SISTEMA DE VENDAS":^50}\033[30m|')
print(f'|{"$"*50}|')
print(f'|{"$"*50}|')
print(f'|{"-"*50}|')


# ============== LAÇO DE REPETIÇÃO =================================================================
while True:
    produto = str(input('| Nome do produto: ')).title().strip()
    preco = float(input('| Preço do produto: R$ '))

    #Variáveis de contagem
    cont += 1
    total += preco

    #Função que coloca o primeiro valor na variavel menos (menor preço)
    if cont == 1:
        menos = preco

    #Função para definir produtos mais caros
    if preco >= 1000:
        mais += 1

    #Função para definir produto mais barato
    if preco < menos:
        menos = preco
        nome = produto

    #Laço para continuar ou interromper o programa
    while True:
        resp = str(input('| Cadastrar mais produtos? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            break
        elif resp == 'N':
            break
        else:
            print(f'|\033[31m{"ATENÇÃO! Dados invalidos. Digite corretamente":^50}\033[30m|')
    if resp == 'N':
        break
# ============== LAYOT DO RODAPÉ ====================================================================
print(f'\033[30m|{"-"*50}|')
print(f'|{"$"*50}|')
print(f'|{"$"*50}|')
print(f'|\033[33m{"RELATÓRIO DAS COMPRAS":^50}\033[30m|')
print(f'|{"$"*50}|')
print(f'|{"$"*50}|')
print(f'|{"-"*50}|')

# ============== CONCLUSÃO DO PROGRAMA ==============================================================
print(f'| \033[33mValor total gasto na compra \033[30mR$ {total}\033[33m reais\033[30m')
print(f'|{"-"*50}|')

#Função para definir possibilidades de conclusões
if mais < 1:
    print(f'| \033[33mNenhum produto custou mais de \033[30mR$ 1.000,00\033[33m reais\033[30m')
elif mais == 1:
    print(f'| {mais} \033[33mproduto custou mais de \033[30mR$ 1.000,00\033[33m reais\033[30m')
else:
    print(f'| {mais} \033[33mprodutos custaram mais de \033[30mR$ 1.000,00\033[33m reais\033[30m')

print(f'|{"-"*50}|')
print(f'| \033[33mO produto mais barato foi: \033[30m{nome}')
print(f'|{"-"*50}|')
print(f'|{"$"*50}|')
print(f'|{"$"*50}|')