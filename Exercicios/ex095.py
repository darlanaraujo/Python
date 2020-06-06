'''
DESAFIO 095

Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização de
DETALHES DO APROVEITAMENTO de cada JOGADOR.
'''
# ================= MODELO CRIADO =====================================================================================
jogadores = {}
gols = []
dados = []

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
    resp = str(input('Cadastrar outro jogador? [S/N]: '))
    if resp in 'nN':
        print('='*50)
        break
    print('='*50)

for p, v in enumerate(dados):
    print(f'Posição {p +1:<2} | Jogador: {dados[p]["nome"]:<8}  |  Gols: {dados[p]["total"]}')

while True:
    cons = int(input('Digite a posição para ver os dados: '))
    for p, v in enumerate(dados):
        if cons == p +1:
            print(f'Jogador: {dados[p]["nome"]}')
            print(f'Nª Partidas: {dados[p]["partidas"]}')
            print(f'Gols: {dados[p]["gols"]}')
            print(f'Total de Gols: {dados[p]["total"]}')

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
