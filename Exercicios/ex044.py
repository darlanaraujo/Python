'''
DESAFIO 044

Elabore um programa que CALCULE O VALOR A SER PAGO por um produto,
considerando o seu PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:

Á VISTA NO DINHEIRO OU CHEQUE: 10% DE DESCONTO;
À VISTA NO CARTÃO: 5% DE DESCONTO;
EM ATÉ 2X NO CARTÃO: PREÇO NORMAL;
3X OU MAIS NO CARTÃO: 20% DE JUROS
'''

# ======================== DEFINIÇÃO DAS CORES DO PROGRAMA =========================================

b   = '\033[30m'
v   = '\033[31m'
vd  = '\033[32m'
a   = '\033[33m'
l   = '\033[m'

# ======================== CABEÇALHO DO PROGRAMA ===================================================

def cabecalho():

    print('{}{}{}{}'.format(b, '|', '='*100, '|'))
    print('{}{}{:^100}{}{}'.format('|', a, 'CONTROLE DE PAGAMENTO', b, '|'))
    print('{}{}{}'.format('|', '='*100, '|'))
    print('{}{}{:^100}{}{}'.format('|', a, 'INFORME O VALOR DO PRODUTO E A FORMA DE PAGAMENTO PARA VER AS OPÇÕES DISPONÍVEIS.', b, '|'))


# ======================== INÍCIO DO PROGRAMA =====================================================

print(cabecalho())
produto = str(input('| INFORME O NOME DO PRODUTO: ')).upper().strip()
print('|'+'='*40)
valor = float(input('| INFORME O VALOR DO PROTUDO: '))
print('|'+'='*100+'|')
print('{}{:^105}{}{}'.format('|', 'OPÇÕES DE PAGAMENTO: \033[33mDINHEIRO - DEBITO - CRÉDITO', b, '|'))
pagamento = str(input('| QUAL A FORMA DE PAGAMENTO: ')).lower().strip()

print('{}{}{}'.format('|', '='*100, '|'))
print('{}{}{:^100}{}{}'.format('|', a, 'INFORMAÇÕES SOBRE O PAGAMENTO', b, '|'))
print('| PRODUTO: {}{}{}'.format(a, produto, b))

# ======================= FORMULAS DO PROGRAMA ======================================================
if pagamento in 'dinheiro':
    desconto = valor / 100 * 10
    soma = valor - desconto
    print('| FORMA DE PAGAMENTO: {}DINHEIRO{}'.format(a, b))
    print('| VALOR TOTAL DO PRODUTO: {}{:.2f}{} REAIS'.format(a, valor, b))
    print('| VALOR DO DESCONTO: {}{:.2f}{} REAIS'.format(a, desconto, b))
    print('| VALOR TOTAL PAGO: {}{:.2f}{} REAIS'.format(a, soma, b))

elif pagamento in 'debito':
    desconto = valor / 100 * 5
    soma = valor - desconto
    print('| FORMA DE PAGAMENTO: {}DÉBITO{}'.format(a, b))
    print('| VALOR TOTAL DO PRODUTO: {}{:.2f}{} REAIS'.format(a, valor, b))
    print('| VALOR DO DESCONTO: {}{:.2f}{} REAIS'.format(a, desconto, b))
    print('| VALOR TOTAL PAGO: {}{:.2f}{} REAIS'.format(a, soma, b))

elif pagamento in 'credito' or 'crédito':
    parcelas = int(input('| QUANTAS PARCELAS DESEJA DIVIDIR O VALOR? {}[2X SEM JUROS OU ATÉ 10X C/ JUROS]{}: '.format(a, b)))
    print('|')
    if parcelas >= 3:
        juros = valor / 100 * 20
        soma = valor + juros
        parcela = soma // parcelas
        print('| FORMA DE PAGAMENTO: {}CRÉDITO COM ACRÉSCIMO DE 20% AO MÊS{}'.format(a, b))
        print('| VALOR TOTAL DO PRODUTO: {}{:.2f}{} REAIS'.format(a, valor, b))
        print('| VALOR TOTAL DO JUROS: {}{:.2f}{} REAIS'.format(a, juros, b))
        print('| VALOR POR PARCELA: {}{:.2f}{} REAIS'.format(a, parcela, b))
        print('| VALOR TOTAL DA COMPRA: {}{:.2f}{} REAIS'.format(a, soma, b))
    elif parcelas == 2:
        soma = valor
        parcela = soma // 2
        print('| FORMA DE PAGAMENTO: {}CRÉDITO 2X SEM JUROS{}'.format(a, b))
        print('| VALOR POR PARCELA: {}{:.2f}{} REAIS'.format(a, parcela, b))
        print('| VALOR TOTAL DA COMPRA: {}{:.2f}{} REAIS'.format(a, soma, b))
    else:
        soma = valor
        print('| FORMA DE PAGAMENTO: {}CRÉDITO À VISTA SEM JUROS{}'.format(a, b))
        print('| VALOR TOTAL DA COMPRA: {}{:.2f}{} REAIS'.format(a, soma, b))

# =================== RODA PÉ DO PROGRAMA ===============================================================================

print('{}{}{}'.format('|', '='*100, '|'))
print('{}{}{:^100}{}{}'.format('|', a, 'FIM DO PROGRAMA', b, '|'))
print('{}{}{}'.format('|', '='*100, '|'))