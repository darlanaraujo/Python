'''
DESAFIO 076

Crie um programa que tenha uma TUPLA ÚNICA com NOMES DE PRODUTOS e seus
respectivos PREÇOS, na sequência.

No final mostre uma LISTAGEM DE PREÇOS, organizando os DADOS EM FORMA
TABULAR.

Ex.
Lápis.......R$  1,75
Borracha....R$ 20,00
'''
# ============= MODELO CRIADO ==============================================
'''
NÃO CONSEGUI CHEGAR A UMA CONCLUSÃO
'''

# ================ MODELO DO CURSO EM VIDEO ===================================================
lista = ('Notebook', 1985.00, 'Mouse s/ fio', 68.00, 'Mochila', 220.00,
         'Fone de ouvido', 175.50, 'Pendrive 8G', 34.00)

print('='*65)
print(f'{"LISTA DE PRODUTOS":^65}')
print('='*65)


for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<50}', end= ' ')
    else:
        print(f'R$ {lista[c]:>7.2f}')

print('='*65)
