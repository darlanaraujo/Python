'''
DESAFIO 093

Crie um programa que gerencia o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o
NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em
CADA PARTIDA. No final, tudo isso será guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS
feitos durante o campeonato.
'''
# ================= MODELO CRIADO =====================================================================================
dados = {}
gols = []
cont = 0

dados['Nome'] = str(input('Nome do Jogador: ')).title().strip()
partidas = int(input('Número de partidas: '))

for c in range(partidas):
    n = int(input(f'Nº de gols na {c + 1}ª partida: '))
    gols.append(n)
    cont += n


dados['Partidas'] = partidas
dados['Gols'] = gols
dados['Total'] = cont

print('-='*25)
print(dados)
print('-='*25)

for itens in dados:
    print(f'{itens}: {dados[itens]}')
print('-='*25)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} partidas')
for p, v in enumerate(gols):
    print(f'    => Na {p +1}ª partida, fez {v} gols.')
print(f'Sendo um total de {dados["Total"]} gols.')

# ================= MELHORIA DO CÓDIGO ================================================================================

# ================= ANAÁLISE DO CÓDIGO ================================================================================

# ================= MODELO CURSO EM VIDEO =============================================================================
