'''
DESAFIO 084

Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS,
guardando tudo em uma LISTA. No final, mostre:

A) QUANTAS PESSOAS fora CADASTRADAS.
B) Uma listagem com as PESSOAS MAIS PESADAS.
C) Uma listagem com as PESSOAS MAIS LEVES.
'''
# ================= MODELO CRIADO =====================================================================================

# ================= MODELO APRIMORADO =================================================================================
# Variável global
pessoas = []
temp = []
pesados = []
leves = []

# Funções de repetição;
def inicio():
    print('=' * 60)
    print(f'{"CADASTRO DE PESSOAS":^60}')
    print('=' * 60)
    cadastro()
    print('=-' * 30)
    conclusao()

def cadastro():
    temp.append(str(input('Nome: ')).title().strip())
    temp.append(float(input('Peso: ')))
    listas()
    print('Dados cadastrados com sucesso!')
    print('=-' * 30)
    return loop()

def listas():
    pessoas.append(temp[:])
    if temp[1] < 70:
        leves.append(temp[:])
    elif temp[1] > 100:
        pesados.append(temp[:])
    temp.clear()

def loop():
    while True:
        resp = str(input('Deseja cadastrar outra? [S/N]: ')).upper().strip()[0]
        if resp == 'S':
            cadastro()
        elif resp == 'N':
            break
        else:
            print('\033[30mATENÇÃO! \033[31mDados inválidos. Digite corretamente.\033[m')
            return loop()
        break

def conclusao():
    print(f'\033[33m{"RELATÓRIO DE CONSLUSÃO":^60}\033[m')
    print('-'*60)
    print(f'Você cadastrou \033[33m{len(pessoas)} pessoas.\033[m')
    print('-'*60)
    if len(pesados) == 1:
        print(f'Foi cadastrado 1 pessoa acima de 100Kg.')
        print(f'    \033[33m>>> Seu nome: \033[30m{pesados[0][0]}\033[m')
    elif len(pesados) > 1:
        print(f'Foi cadastrado {len(pesados)} pessoas acima de 100Kg.')
        print(f'    \033[33m>>> Seus nomes: ', end='')
        for pos, p in enumerate(pesados):
            print(f'\033[30m[{p[0]}]\033[m', end=' ')
    else:
        print('Não foi cadastrado nenhuma pessoa acima de 100Kg.')
    print()
    print('-'*60)

    if len(leves) == 1:
        print(f'Foi cadastrado 1 pessoa abaixo de 70Kg.')
        print(f'    \033[33m>>> Seu nome: \033[30m{leves[0][0]}\033[m')
    elif len(leves) > 1:
        print(f'Foi cadastrado {len(leves)} pessoas abaixo de 70Kg.')
        print(f'    \033[33m>>> Seus nomes: ', end='')
        for pos, p in enumerate(leves):
            print(f'\033[30m[{p[0]}]\033[m', end=' ')
    else:
        print('Não foi cadastrado nenhuma pessoa abaixo de 70Kg.')

# Início do programa;
inicio()

# ================== ANÁLISE DO CÓDIGO ================================================================================
'''
Nesse código o principio seria o mesmo, é claro que eu pulei etapas uma vez que usei uma função DEF que ainda não foi
passada em aula, por esse motivo meu código não pode ser comparado ao exigido. Mas em relação a forma de pensar no
código eu defini alguns elementos mais elaborados, como padrão para o nome, opções caso algum peso não fosse atingido.
'''

# OBSERVAÇÃO
'''O exemplo mostrado na aula, ele fez o exercicio como se existisse um peso base, sendo
100Kg para maior e 70Kg para menor. Por esse motivo meu código segue esse formato, mas
seria fácil de ser alterado para simplesmente mostrar o maior e o menor.'''

# ================== MODELO CURSO EM VÍDEO ============================================================================
'''temp = []
princ = []
maio = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maio = men = temp[1]
    else:
        if temp[1] > maio:
            maio = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break
print('=-'*30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {maio}Kg. Peso de ', end= '')
for p in princ:
    if p[1] == maio:
        print(f'[{p[0]}]', end= ' ')
print()
print(f'O menor peso foi {men}Kg. Peso de ', end= '')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end= ' ')
print()'''