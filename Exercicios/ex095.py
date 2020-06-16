'''
DESAFIO 095

Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização de
DETALHES DO APROVEITAMENTO de cada JOGADOR.
'''
# ================= MODELO CRIADO =====================================================================================
'''jogadores = {}
gols = []
dados = []

print('\033[30m='*50)
print(f'\033[33m{"CADASTRO DE JOGADORES":^50}\033[30m')
print('='*50)
while True:
    jogadores['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input('Nº partidas: '))
    jogadores['partidas'] = partidas
    print('='*50)
    cont = 0

    for c in range(partidas):
        n = int(input(f'==> Nº de gols na {c +1} partida: '))
        cont += n
        gols.append(n)

    jogadores['gols'] = gols[:]
    gols.clear()
    jogadores['total'] = cont
    dados.append(jogadores.copy())

    print('='*50)
    while True:
        resp = str(input('Cadastrar outro jogador? [S/N]: ')).upper()[0]
        if resp in 'SN':
            print('=' * 50)
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
        print('='*50)

print('\033[30m='*50)
print(f'\033[33m{"RELATÓRIO DE JOGADORES":^50}\033[30m')
print('='*50)
for p, v in enumerate(dados):
    print(f'Posição \033[33m{p +1:<2}\033[30m | Jogador: \033[33m{dados[p]["nome"]:<8}\033[30m  |  Gols: \033[33m{dados[p]["total"]}\033[30m')

while True:
    print('='*50)
    cons = int(input('\033[33mDigite a posição para ver os dados:\033[30m '))
    print('='*50)
    for p, v in enumerate(dados):
        if cons == p +1:
            print(f'Jogador: \033[33m{dados[p]["nome"]}\033[30m')
            print(f'Nª Partidas: \033[33m{dados[p]["partidas"]}\033[30m')
            print(f'Total de Gols: \033[33m{dados[p]["total"]}\033[30m')
            print(f'Gols por partida:')
            for p, v in enumerate(dados[p]['gols']):
                print(f'    >> Na \033[33m{p +1}ª \033[30mpartida \033[33m{v}\033[30m')
        else:
            print(f'Não há cadastro na posição {cons}')'''

# ================= MELHORIA DO CÓDIGO ================================================================================
'''from time import sleep

jogador = dict()
dados = list()
gols = list()

def cabecalho(txt):
    print('\033[30m='*50)
    print(f'\033[33m{txt:^50}')
    print('\033[30m='*50)


def inicio():
    menu()

def menu():
    cabecalho('ESTATISTICAS DE JOGADORES')
    print('A) CADASTRAR JOGADOR:')
    print('B) CONSULTAR CADASTROS:')
    print('C) CONSULTAR JOGADOR:')
    print('D) VER TODOS:')
    print('E) SAIR:')
    print('='*50)
    comando()

def verificacao():
    if dados == []:
        print('\033[31mNenhum jogador cadastrado!\033[30m')
        confirma('\033[33mDeseja fazer um novo cadastro? \033[30m[S/N]: ')


def atleta():
    cabecalho('CONSULTA POR JOGADOR')
    verificacao()
    nome = str(input('Nome do jogador: ')).title().strip()
    print('#'*50)
    print('#'*50)
    for p, v in enumerate(dados):
        #print(f'Na posição {p} encontrei {v}')
        if nome in dados[p]['nome']:
            print(f'\033[33mNOME: \033[30m{v["nome"]} | \033[33mNº PARTIDAS: \033[30m{v["partidas"]} | \033[33mNº GOLS: \033[30m{(v["total"])}')
            print('-'*50)
            print('>>> \033[33mGols por partida:\033[30m')
            media = v['media']
            for p, v in enumerate(v['gols']):
                print(f'     >> Na \033[33m{p +1}ª \033[30mpartida: \033[33m{v}\033[30m')
            print('-'*50)
            print(f'>>> Aproveitamento de \033[33m{media:.2f} gols \033[30mpor partida')
            print('-'*50)

            while True:
                resp = str(input('DESEJA ACRESCENTAR PARTIDA? [S/N]: ')).upper().strip()[0]
                if resp in 'SN':
                    break
                print('ERRO! Digite apenas S ou N.')
            if resp == 'S':
                dados[p]['partidas'] += 1
                n = int(input('Número de gols feito na partida: '))
                gols.append(n)
                dados[p]['gols'] += gols[:]
                dados[p]['total'] += n
                dados[p]['media'] = dados[p]['total'] / dados[p]['partidas']
                print('-'*50)
                print('Inserindo dados', end='')
                for c in range(0, 5):
                    print('.', end='')
                    sleep(0.5)
                print('\nDados inseridos com sucesso!')
                sleep(1)
                menu()
            elif resp == 'N':
                menu()

    else:
        print(f'O jogador \033[33m{nome} \033[30mnão está cadastrado!')
        confirma(f'\033[33mDESEJA CADASTRAR O JOGADOR \033[34m{nome}? \033[30m[S/N]: ')


def consulta():
    cabecalho('JOGADORES CADASTRADOS')
    verificacao()
    for p, v in enumerate(dados):
        print(f'Nome: {dados[p]["nome"]}')
    sleep(2)
    menu()


def todos():
    cabecalho('RELATÓRIO GERAL DOS JOGADORES')
    verificacao()
    for p, v in enumerate(dados):
        print(f'Nome: \033[34m{dados[p]["nome"]:<10} \033[30m| Partidas: {dados[p]["partidas"]:<3} | Nº de Gols: {dados[p]["total"]:<3} \n\033[33mMédia por Partida: \033[30m{dados[p]["media"]:.2f}')
        print('~'*50)
    print('-'*50)
    print('\033[31mPara consular dados individuais digite o nome\ndo jogador:\033[30m')
    atleta()



def cadastro():
    cabecalho('CADASTRO DE JOGADORES')
    jogador['nome'] = str(input('Nome do Jogador: ')).title().strip()
    partidas = int(input('\033[33mNº de partidas: \033[30m'))
    jogador['partidas'] = partidas
    
    cont = 0
    for c in range(partidas):
        n = int(input(f'Nº de gols na {c +1}ª partida: '))
        gols.append(n)
        cont += n
    jogador['gols'] = gols[:]
    jogador['total'] = cont
    jogador['media'] = jogador['total'] / jogador['partidas']
    gols.clear()
    dados.append(jogador.copy())
    jogador.clear()

    print('Inserindo dados', end='')
    for c in range(0, 5):
        print('.', end='')
        sleep(0.5)
    print('\nDados inseridos com sucesso!')
    sleep(1)

    confirma('\033[33mContinuar cadastrando? \033[30m[S/N]: ')
        

def confirma(txt):
    print('=' * 50)
    while True:
        resp = str(input(txt)).upper().strip()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO! Digite apenas S ou N.\033[30m')
    if resp == 'S':
        cadastro()
    if resp == 'N':
        menu()


def comando():
    while True:
        resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).upper().strip()[0]
        if resp in 'ABCDE':
            break
        print('\033[31mERRO! Digite corretamente as opções validas!\033[30m')
        print('='*50)
    if resp == 'A':
        cadastro()
    elif resp == 'B':
        consulta()
    elif resp == 'C':
        atleta()
    elif resp == 'D':
        todos()
    elif resp == 'E':
        print('Finalizando', end='')
        for c in range(0, 5):
            print('.', end='')
            sleep(0.5)
        sleep(1)


# Início do programa;
inicio()'''
# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos gols na partida {c}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
