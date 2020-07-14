from modulos.cadastro import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt') # reading text ou leitura texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+') # write text ou escreve texto - O + é para que, caso o arquivo não exista, ele cria.
        a.close()
    except:
        print(f'Houve um ERRO na criação do arquivo {nome}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt') # reading text ou leitura texto
    except:
        print(f'ERRO ao tentar ler o arquivo {nome}!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        #print(a.readlines()) #Essa função faz mostrar o conteúdo do arquivo em linha
        #print(a.read()) #Essa função mostra o conteúdo na forma como está.
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<15} | Idade: {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at') # append text ou Acrescentar Texto
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao adicionar um novo arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()