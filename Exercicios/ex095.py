'''
DESAFIO 095

Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização de
DETALHES DO APROVEITAMENTO de cada JOGADOR.
'''
# ================= MODELO CRIADO =====================================================================================
jogadores = {}
gols = []
dados = []
cont = 0
while True:
    jogadores['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input('Nº partidas: '))
    jogadores['partidas'] = partidas
    print('='*50)

    for c in range(partidas):
        n = int(input(f'==> Nº de gols na {c +1} partida: '))
        cont += n
        gols.append(n)

    jogadores['gols'] = gols
    jogadores['total'] = cont
    dados.append(jogadores.copy())

    print('='*50)
    resp = str(input('Cadastrar outro jogador? [S/N]: '))
    if resp in 'nN':
        print('='*50)
        break
    print('='*50)

for p, v in enumerate(dados):
    print(f'Posição {p} | Jogador: {dados[p]["nome"]}  |  Gols: {dados[p]["total"]}')

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
