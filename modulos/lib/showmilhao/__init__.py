# ================= FUNÇÕES GLOBAIS DO JOGO ===========================================================================
# Biblioteca global
from time import sleep
from random import randint

# Definição de cores
cor = ('\033[m'     # 0 = Sem cor
       '\033[30m'   # 1 = Branco
       '\033[31m'   # 2 = Vermelho
       '\033[32m'   # 3 = Verde
       '\033[33m'   # 4 = Amarelo
       '\033[34m'   # 5 = Azul
       '\033[35m'   # 6 = Roxo
       )

# Varial global
arq = 'jogoshowmilhao.txt'

# ================= PERGUNTAS DO JOGO =================================================================================
pergunta_niv1 = ['Qual o meu nome? \nA) Darlan Araujo \nB) Fabil Santana \nC) Antônio Silva \nD) José Pereira',
                 'Qual cidade eu nasci? \nA) Eunápolis \nB) Itamaraju \nC) Nova Alegria \nD) Além Paraíba',
                 'Qual a minha idade? \nA) 17 anos \nB) 24 anos \nC) 30 anos \nD) 35 anos',
                 ]

resposta_niv1 = ['A',
                'B',
                'D',
                 ]

pergunta_niv2 = [
                 ]

resposta_niv2 = [
                 ]

pergunta_niv3 = [
                 ]

resposta_niv3 = [
                 ]

pergunta_niv4 = [
                 ]

resposta_niv4 = [
                 ]

pergunta_final = [
                 ]

resposta_final = [
                 ]

sorteio = randint(0, 2)

valores = [1000, 2000, 3000, 5000, 10000, 20000, 30000, 50000, 100000, 200000, 300000, 500000, 1000000]

premio = 0
# ================= FUNÇÕES GERAIS DO JOGO ============================================================================
def inicio():
    menu()


def start():
    print('-' * 60)
    while True:
        sleep(1)
        resp = str(input('Aperte ENTER para retornar ao menu inicial >>>'))
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
    try:
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
    except:
        erro('\033[31mHouve um erro com a sua escolha. \033[30mTente novamente')
        sleep(1)
        return inicio()


def erro(msg):
    linha()
    print(f'\033[31m{msg}\033[30m')
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


# ================= FUNÇÕES DO SISTEMA DO JOGO ========================================================================
def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


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


def cadastrar(arq):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        cabeçalho('=', 'CADASTRO DE JOGADOR')
        cont = 1
        nome = str(input('Jogador: ')).strip().title()

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
            return capa()


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


# ======================= FUNÇÕES DE PERGUNTAS DO JOGO ================================================================
def final():
    cabeçalho('=', 'SHOW DO MILHÃO - CONFIRA SEU PREMIO')
    print(f'Meuns parabéns você ganhou {premio}')


def capa():
    cabeçalho('=', 'PRIMEIRA RODADA NIVEL 1')
    while True:
        resp = str(input('VAMOS COMEÇAR? [S/N]: ')).upper().strip()[0]
        linha()
        if resp == 'S':
            perguntas()
        elif resp == 'N':
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
            erro('ERRO! Escolha uma opção válida!')


'''def pergunta1():
    cabeçalho('=', f'PRIMEIRA PERGUNTA VALENDO {moeda(valores[0])} REAIS')
    pergunta1 = pergunta_niv1[sorteio]
    resposta1 = resposta_niv1[sorteio]

    # FERRAMENTA DE TESTE
    #print(resposta1)

    print(pergunta1)
    linha()
    resp = str(input('Escolha a opção correta: ')).upper().strip()[0]
    linha()
    if resp == resposta1:
        print('PARABÉNS! Você acertou.')
        premio += valores[0]
        pergunta2()
    else:
        print('Que pena, você errou!')'''

def perguntas():
    for p, v in enumerate(valores):
        cabeçalho('=', f'{p + 1}ª PERGUNTA VALENDO {moeda(valores[p])} REAIS')
        if p <= 3:
            pergunta1 = pergunta_niv1[sorteio]
            resposta1 = resposta_niv1[sorteio]

            # FERRAMENTA DE TESTE
            #print(resposta1)

            print(pergunta1)
            linha()
            resp = str(input('Escolha a opção correta: ')).upper().strip()[0]
            linha()
            if resp == resposta1:
                print(f'PARABÉNS! Você acertou. Acaba de ganhar {moeda(valores[p])}')

            else:
                if p <= 3:
                    print('Que pena, você errou! Você não ganhou nada.')
                elif p <= 11:
                    print(f'Que pena, você errou! Seu premio é de {moeda(valores[p -1])}')
                else:
                    print('Que pena, você errou! Você perdeu tudo!.')
                break
        elif p == 4:
            resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
            if resp == 'S':
                print('teste em construção!')
