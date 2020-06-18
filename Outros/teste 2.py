dados = []
jogador = {'jogador': 'Darlan', 'partida': 2, 'gols': [1, 0], 'total': 2, 'media': 0.5}
dados.append(jogador.copy())
jogador.clear()

jogador = {'jogador': 'Davi', 'partida': 2, 'gols': [3, 2], 'total': 5, 'media': 2.5}
dados.append(jogador.copy())

for p, v in enumerate(dados):
    print(f'Na posição: {p}, encontrei {v}')
for k, v in jogador.items():
    print(f'Na chave {k} encontrei {v}')

