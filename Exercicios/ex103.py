'''
DESAFIO 103

Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: O NOME de um jogador e
quantos GOLS ele marcou.

O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha sido informado corretamente.
'''
# ================ CÓDIGO BASE ========================================================================================
def ficha(n='<Desconhecido>', g=0):
    '''
        --> A função ficha recebe a informação do usuário com o nome do jogador e quantos gols ele fez. Caso algum
        parâmetro não seja preenchido, ele sera substituido pelo parâmetro estipulado.
    :param n: Nome do jogador ou caso não seja informado recebe o texto pré-definido pelo programa.
    :param g: Número de gols ou caso não seja informado recebe 0.
    :return: Mostra na tela os dados do jogador.
    '''
    print(f'O jogador {n} fez {g} gols.')

jogador = str(input('Nome do jogador: ')).title().strip()
gols = str(input('Número de gols: '))

if jogador == '' and gols == '':
    ficha()
elif jogador == '':
    ficha(g=gols)
elif gols == '':
    ficha(n=jogador)
else:
    ficha(jogador, gols)

# ================ CÓDIGO MELHORADO ===================================================================================

# ================ ANÁLISE DO CÓDIGO ==================================================================================
'''
Análisando os dois código, a diferença fica apenas pela forma como a leitura dos parâmetros, aonde no meu eu uso 4
possíveis resultados, já no código do curso, ele usou uma leitura que ainda não entendi. Um ponto importante foi ter
tentado todas as possibilidades para usar a chamada dos gols como int e após vários erros cheguei a conclusão que só
daria certo usando uma string, e o curso usou o mesmo recurso.
'''
# ================ CÓDIGO CURSO EM VÍDEO ==============================================================================
'''def ficha(jog='<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)'''