'''
DESAFIO 073

Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da
tabela do BRASILEIRÃO, na ordem de colocação. Depois mostre:

A) APENAS OS 5 PRIMEIROS COLOCADOS.
B) OS ÚLTIMOS 4 COLOCADOS.
C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE.
**OU UM TIME DIGITADO PELO TECLADO.
'''
# ==================== TUPLA GLOBAL =========================================================
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo',
          'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco Da Gama',
          'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense',
          'Avaí')

# =================== MODELO CRIADO =========================================================
'''print(f'='*100)
print(f'{"TABELA DO BRASILEIRÃO 2019":^100}')
print(f'='*100)
print('Os 5 primeiros colocados do Brasileirão 2019:')
for col, tab in enumerate(tabela[0:5]):
    print(f'{col +1} - {tab} |', end= ' ')

print()
print('-'*100)

print('Os últimos 4 colocados do Brasileirão 2019')
for col, tab in enumerate(tabela[16:20]):
    print(f'{col+17} - {tab} |', end= ' ')

print()
print('-'*100)

print('Tabela do Brasileirão em ordem alfabetica')
ordem = sorted(tabela[:])
for pos, ord in enumerate(ordem[:]):
    print(f'{ord}', end= '')
    if pos != 19:
        print(' -', end= ' ')
    else:
        print('.')

print()
print('-'*100)

print('Posição da chapecoense na tabela:')
print(f'Posição {tabela.index("Chapecoense")+1}º colocado')

print()
print('-'*100)'''

# ================== MODELO CURSO EM VIDEO ======================================================
'''print('=-'*30)
print(f'Lista de times: \n{tabela}')
print('=-'*30)
print(f'Os 5 primeiros times da tabela: \n{tabela[0:5]}')
print('=-'*30)
print(f'Os últimos 4 colocados: \n{tabela[-4:]}')
print('=-'*30)
print(f'Lista dos times em ordem alfabética: \n{sorted(tabela)}')
print('=-'*30)
print(f'A Chapecoense está na {tabela.index("Chapecoense") +1}ª posição')'''

# ================== MELHORIAS DO MEU MODELO CRIADO =============================================

# FUNÇÃO DE DEFINIÇÃO
def nome():
    time = str(input('Digite o nome do time: ')).title().strip()
    if time in tabela:
        posicao = tabela.index(time)
        print(f'A posição do {time} é {posicao +1}º colocado.')
    else:
        print(f'\033[31mATENÇÃO! Digite corretamente ou o time {time} não está na primeira divisão desse ano.\033[m')
        return nome()

    return loop()

def colocacao():
    num = int(input('Qual a colocação: '))

    if num <= len(tabela):
        time = tabela[num - 1]
        print(f'Na {num}º colocação está o time {time}.')
    elif num > len(tabela):
        print('\033[31mATENÇÃO! A tabela do Brasileiro vai de 1º a 20º colocado.\033[m')
        return colocacao()

    return loop()

def primeiro():
    print(f'Os 5 primeiros colocados: \n{tabela[0:5]}')
    return loop()

def ultimos():
    print(f'Os últimos 4 colocados: \n{tabela[-4:]}')
    return loop()

def ordem():
    print(f'Lista dos times em ordem alfabética: \n{sorted(tabela)}')
    return loop()

def pergunta():
    print('=-' * 70)
    print('[1] PESQUISAR PELO NOME:'
          '\n[2] PESQUISAR PELA COLOCAÇÃO:'
          '\n[3] Ver OS 5 PRIMEIROS COLOCADOS:'
          '\n[4] VER OS 4 ÚLTIMOS COLOCADOS:'
          '\n[5] ORGANIZAR POR ORDEM ALFABÉTICA:')
    print()
    resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).upper().strip()[0]
    print('=-' * 70)
    if resp == '1':
        nome()
    elif resp == '2':
        colocacao()
    elif resp == '3':
        primeiro()
    elif resp == '4':
        ultimos()
    elif resp == '5':
        ordem()
    else:
        print('\033[31mATENÇÃO! Informação inválida, opções \033[33m[1] [2] [3] [4] [5].\033[m')
        return pergunta()

def loop():
    while True:
        print('=-' * 70)
        resp = str(input('Deseja consultar outro time? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            return pergunta()
        elif resp == 'N':
            print('Fim do programa !')
            break
        else:
            print('\033[31mATENÇÃO! Informação inválida, digite corretamente.\033[m')

# ================== INÍCIO DO PROGRAMA ====================================
print('='*100)
print(f'{"ESCOLHA O TIME QUE DESEJE SABER SUA POSIÇÃO NA TABELA:":^100}')
pergunta()
