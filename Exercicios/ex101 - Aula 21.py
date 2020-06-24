'''
DESAFIO 101

Crie um programa que tenha uma função chamada VOTO() que vai receber como PARÂMETRO o ANO DE NASCIMENTO de uma pessoa,
RETORNANDO um valor LITERAL indicando se uma essoa tem voto, MEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
# ================== CÓDIGO BASE ======================================================================================
from datetime import date

def voto(ano):
    '''
        --> A função recebe os dados da variável e faz uma veficação da data atual pela função data ano, e de acordo
        com a idade retorna o resultado.
    :param ano: Recebe a variável digitada pelo usuário
    :return: De acorodo com a soma da idade mostra se a pessoa NÃO VOTA - VOTO OPCIONAL - VOTO OBRIGATÓRIO
    '''
    hoje = date.today().year
    idade = hoje - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        #print('NÃO VOTA!')
        return 'NÃO VOTA'
    elif idade == 16 or idade < 18 or idade >= 65:
        #print('VOTO OPCIONAL.')
        return 'VOTO OPCIONAL'
    else:
        #print('VOTO OBRIGATÓRIO.')
        return 'VOTO OBRIGATÓRIO'

help(voto)
ano = int(input('Em que ano você nasceu? '))
#IMPORTANTE! Para usar o retorno da função para ser mostrado, só funiona se abaixo a chamada da função estiver no print.
print(voto(ano))
voto(ano)
    
# ================== CÓDIGO MELHORADO =================================================================================

# ================== ANÁLISE DO CÓDIGO ================================================================================
'''

'''
# ================== CÓDIGO CURSO EM VÍDEO ============================================================================
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))