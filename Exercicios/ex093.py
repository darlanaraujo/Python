'''
DESAFIO 093

Crie um programa que gerencia o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o
NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em
CADA PARTIDA. No final, tudo isso será guardado em um DICIONÁRIO, incluindo o TOTAL DE GOLS
feitos durante o campeonato.
'''
# ================= MODELO CRIADO =====================================================================================
'''dados = {}
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
print(f'Sendo um total de {dados["Total"]} gols.')'''

# ================= MELHORIA DO CÓDIGO ================================================================================
'''
A melhoria do código vai ficar para o próximo exercício que solicita essa melhoria.
'''
# ================= ANAÁLISE DO CÓDIGO ================================================================================
'''
Os códigos são parecidos nas funções. Gostei do recurso que ele usou para somar os valores dentro da lista usando uma
função sum(). 
'''
# ================= MODELO CURSO EM VIDEO =============================================================================
jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'     Quantos gols na partida {c}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'      => Na partida {i}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')