'''
JOGO DA FORCA 1.0

O código do jogo vai ser escrito baseado no vídeo do youtube (Smart School).
'''

import os, random, time

#Variáveis globais;

palavras = [

    ['O', 'S', 'e', 'n', 'h', 'o', 'r', ' ', 'é', ' ', 'b', 'o', 'm'],
    ['D', 'a', 'v', 'i', ' ', 'A', 'r', 'a', 'u', 'j', 'o'],
    ['E', 'u', 'n', 'á', 'p', 'o', 'l', 'i', 's'],
    ['P', 'e', 'n', 's', 'o', ' ', 'l', 'o', 'g', 'o', ' ', 'e', 'x', 'i', 's', 't', 'o']

]

tentativas = 0
palavras_certas = 0
palavras_erradas = 0
palavra_em_jogo = None

vidas = 3
pontos = 0
limpa = "os.system('cls' if os.name == 'nt' else clear )"
#limpa = "os.system('cls')"

#============================= INTERFACE ===============================

def cabecalho():
    print()
    print('{}{}{}'.format('|', '='*100, '|'))
    print('{}{:^100}{}'.format('|', 'JOGO DA FORCA - VERSÃO 1.0', '|'))
    print('{}{}{}'.format('|', '='*100, '|'))

def placar():
    cabecalho()
    print('{}{:^100}{}'.format('|', 'VIDAS: '+str(vidas), '|'))
    print('{}{}{}'.format('|', '='*100, '|'))

# ========================== FUÇÕES AUXILIARES ==========================

def pergunta(questao, erro = '\033[31mAtenção! Digite \033[30m"S" \033[31mpara sim ou \033[30m"N" \033[31mpara não.\033[m'):

    while True:
        try:
            resposta = input(questao)
            if resposta[0] == 'S' or resposta[0] == 's':
                return True
            elif resposta[0] == 'N' or resposta[0] == 'n':
                return False
            else:
                print(erro)
        except:
            print('\033[31mCertifique-se de que digitou um valor correto.\033[m')

# ========================= FUNÇÕES PRINCIPAIS ==========================

# Retorna o valor inicial da variável global palavras;
def reset_palavras():

    palavras = [

        ['O', 'S', 'e', 'n', 'h', 'o', 'r', ' ', 'é', ' ', 'b', 'o', 'm'],
        ['D', 'a', 'v', 'i', ' ', 'A', 'r', 'a', 'u', 'j', 'o'],
        ['E', 'u', 'n', 'á', 'p', 'o', 'l', 'i', 's'],
        ['P', 'e', 'n', 's', 'o', ' ', 'l', 'o', 'g', 'o', ' ', 'e', 'x', 'i', 's', 't', 'o']

    ]

    return palavras

#Conjunto de funções que tratam as palavras do jogo.
def gerenciador_de_palavras():

    # Função Limpar a tela;

    eval(limpa) ; cabecalho()

    contador, palavras_recebidas = 0, []

    # Função pegar palavras digitadas pelo usuário;
    while True:
        contador += 1
        palavras_recebidas += [input('Digite a '+str(contador)+'ª palavra ou frase desejada: ')]

        if not pergunta('Deseja adicionar outra palavra ou frase? [S/N]: '):
            break

    # Palavras Tratadas: Aqui separamos as palavras digitadas pelo usuário fazendo com que o programa a divida em letras;

    palavras_tratadas, palavra_tratada = [], []

    for palavra in palavras_recebidas:
        for letra in palavra:
            palavra_tratada.append(letra)
        palavras_tratadas += [palavra_tratada]
        palavra_tratada = []

    #Essa função verifica se ao escolher digitar uma palavra o jogador a deixou em branco.
    lista_vazia = 0
    for palavra in palavras_tratadas:
        if palavra == []:
            lista_vazia += 1

    #Essa função elimina a lista vazia identificada no código acima.

    for i in range(lista_vazia): #Aqui é criadoum laço 'for' e uma lista 'i' e uma busca 'range' se houver 'in' dentro da variável 'lista_vazia'.
        for j in range(len(palavras_tratadas)): #for J é uma lista. Range percorre uma informação dentro do laço. A função Len, lê as palavras dentro da variável.
            if palavras_tratadas[j] == []: #'if' Se dentro da variável, dentro do indice 'j' for igual 'vazio'.
                del (palavras_tratadas[j]) #Deleta os espaços vazios dentro da variável palavras_tratadas.
                break #Apos percorrer esse laço, identificar e excluir os espaços vazios se houver. Ele para a busca.

    return palavras_tratadas

#Definição da função que vai colocar as palavras da lista em jogo.
def palavra_em_jogo(palavras):

    #Essa função retorna as palavras da variável 'palavras' de forma aleatória 'random'
    #e o 'randint' ler a quantidade de palavras dentro dessa lista, já o -1 é para não escapar do indice.
    return palavras[random.randint(0, len(palavras) -1)]

#Definição de função que gera a quantidade de erros que o jogador pode cometer por jogada
#Também tem a função para automatizar o calculo de acordo com o tamanho da palavra sorteada quantos erros são permitidos.

def quantidade_de_tentativas(palavra_em_jogo):
    #Aqui o programa lê a quantidade de caracteres da palavra sorteada. Se for menor que 6 são 2 tentativas.
    if len(palavra_em_jogo) <= 6:
        tentativas = 2
    else:
        #Essa função determina que as tentativas vão de 2 a 6 erros.
        #len Lê os caracteres dentro da palavra em jogo e divide entre 2 a 6 tentativas.
        tentativas = len(palavra_em_jogo) // random.randint(2, 6)

        #Caso a divisão seja 1 tentativa, essa função acrescenta mais 1.
        if tentativas <= 2:
            tentativas += 2

#========================================================================

while True:
    eval(limpa) ; cabecalho() #; placar()

# Pergunta se deseja adicionar mais palavras ao jogo;
    print('\033[33mO jogo já tem \033[30mpalavras predefinidas. \033[33mVocê pode usá-las ou digitar novas.\033[m')
    print()
    if pergunta('Deseja adicionar mais palavras ao jogo? [S/N]: '):

        #Essa variável substitui as palavras pré-definidas do jogo.
        palavras = gerenciador_de_palavras()

            # Verificar se as palavras não estão vazias;
        if palavras == []:
            palavras = reset_palavras() #Essa função faz com que as palavras pré-definidas sejam executadas.
            print('\033[33mComo nenhuma \033[30mpalavra foi adicionada\033[33m, será usado as \033[30mpalavras predefinidas do jogo.\033[m')
            time.sleep(3)

    print(palavra_em_jogo(palavras))
    break

