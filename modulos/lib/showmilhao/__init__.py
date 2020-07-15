# ================= FUNÇÕES GLOBAIS DO JOGO ===========================================================================
# Biblioteca global
from time import sleep

# Varial global
arq = 'jogoshowmilhao.txt'

# ================= FUNÇÕES GERAIS DO JOGO ============================================================================
def inicio():
    menu()


def start():
    print('-' * 60)
    while True:
        sleep(1)
        resp = str(input('Aperte ENTER para retornar ao menu inicial:'))
        if resp == '':
            return inicio()
        else:
            erro('\033[31mERRO! Aperte \033[33mENTER\033[m')


def menu():
    cabeçalho('=', 'JOGO SHOW DO MILHÃO - V1.0')
    manual()
    print('\033[33mA) \033[30mCOMEÇAR NOVO JOGO')
    print('\033[33mB) \033[30mRANKING DOS JOGADORES')
    print('\033[33mC) \033[30mMANUAL DO JOGO')
    print('\033[33mD) \033[30mSAIR DO JOGO')
    linha()
    while True:
        resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).strip().upper()[0]
        if resp == 'A':
            arquivo(arq)
        elif resp == 'B':
            placar(arq)
        elif resp == 'C':
            regras()
        elif resp == 'D':
            linha()
            print('Saindo do jogo', end='')
            sleep(.5)
            for c in range(1, 6):
                print('.', end='')
                sleep(.5)
            sleep(.5)
            print('Até a próxima!')
            break
        else:
            erro('ERRO! Dados inválidos!')


def erro(msg):
    linha()
    print(f'\033[31m{msg}\033[m')
    linha()


def manual():
    print('Seja bem-vindo ao Jogo Show do Milhão!')
    print()
    print('A cada rodada você responderá a uma pergunta \nvalendo premios em reais.')
    print()
    print('Bom jogo e boa Sorte!')
    linha()


def regras():
    print('Texto com as regras')
    return start()


def cabeçalho(caractere, msg):
    linha(caractere)
    print(msg.center(60))
    linha(caractere)


def linha(caractere='-', tam=60):
    print(caractere * tam)


# ================= FUNÇÕES DE FERRAMENTAS DO JOGO ====================================================================
def arquivo(arq):
    # Função para definir o nome do arquivo aonde os dados dos jogadores ficarão salvos.
    if not arquivoexiste(arq):
        criararquivo(arq)
    else:
        cadastrar(arq)

def arquivoexiste(arq):
    # Função que verifica se o arquivo (banco de dados) existe.
    try:
        a = open(arq, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq):
    # Função que cria o arquivo (banco de dados) caso não exista.
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo {arq}')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def cadastrar(arq, premio='R$ 0,00'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        cabeçalho('=', 'CADASTRO DE JOGADOR')
        cont = 1
        print(arq.count('Jogador'))
        print(cont)
        nome = str(input('Jogador: '))

        if nome == '':
            nome = f'Jogador {cont}'
            cont += 1
        try:
            a.write(f'{nome};{premio}\n')
        except:
            print(f'ERRO ao cadastrar o jogador {nome}')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
            return start()


def placar(arq):
    try:
        a = open(arq, 'rt')
    except:
        print(f'Houve um erro ao tentar ler o arquivo {arq}')
    else:
        cabeçalho('=', 'RANKING DE JOGADORES')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Jogador: {dado[0]:<15} | Premio: {dado[1]:>5}')
        return start()

