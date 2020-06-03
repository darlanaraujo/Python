'''
DESAFIO 089

Crie um programa que leia NOME E DUAS NOTAS de vários alunos e guarde tudo em uma
LISTA COMPOSTA. No final, mostre um BOLETIM contendo a MÉDIA de cada um e permita
que o usuário possa mostrar as NOTAS de CADA ALUNO INDIVIDUALMENTE.
'''
# =============== MODELO CRIADO ===========================================================================
# PROGRAMA
'''alunos = []
nome = []

print('='*60)
print(f'{"CADASTRO DE ALUNOS":^60}')
print('='*60)
while True:
    nome.append(str(input('Nome do aluno: ')).title().strip())
    nome.append(float(input('Primeira nota: ')))
    nome.append(float(input('Segunda nota: ')))
    media = (nome[1] + nome[2]) / 2
    nome.append(media)
    alunos.append(nome[:])
    nome.clear()
    print('Aluno cadastrado com sucesso!')
    print('='*60)

    resp = str(input('Deseja cadastrar outro aluno? [S/N] '))
    if resp in 'nN':
        break

print('='*60)
print(f'{"BOLETIM DOS ALUNOS":^60}')
print('='*60)
print(f'\033[33m{"POSIÇÃO":<20}{"NOME":^20}{"MÉDIA":>18}\033[m')
print('-'*60)
for p, a in enumerate(alunos):
    print(f'{p+1:<20} {a[0]:^20}{a[3]:>18}')

print('='*60)
sair = 0
while resp != 999:
    print('\033[33mPara sair do programa digite: \033[30m999\033[m')
    resp = int(input('Escolha a posição para ver a nota do aluno: '))
    print('='*60)
    for p, a in enumerate(alunos):
        if resp == p+1:
            print(f'Nome: {a[0]} | Primeira nota: {a[1]} | Segunda nota: {a[2]}')
            print('='*60)

print('Fim do programa!')'''

# =============== MODELO APRIMORADO ========================================================================
# PROGRAMA
alunos = []
temp = []

def inicio():
    print('='*40)
    print(f'\033[33m{"CADASTRO DE ALUNOS":^40}\033[m')
    print('='*40)
    cadastro()

def cadastro():
    temp.append(str(input('Nome do aluno: ')).title().strip())
    temp.append(float(input('Primeira Nota: ')))
    temp.append(float(input('Segunda Nota: ')))
    media = (temp[1] + temp[2]) / 2
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()
    confirmacao('Continuar cadastrando? [S/N]: ', cadastro, menu)

def exit():
    print('='*40)
    ex = str(input('Continuar cadastrando? [S/N]: ')).strip()
    print('='*40)
    if ex in 'Ss':
        cadastro()
    elif ex in 'Nn':
        menu()
    else:
        print('\033[30mAtenção! \033[31mDados invalidos, digite corretamente.\033[m')
        return exit()

def pesquisa():
    print('='*40)
    print(f'{"ALUNOS CADASTRADOS":^40}')
    print('='*40)
    for c in alunos:
        print(c[0])
    nomes()

def nomes():
    print('='*40)
    aluno = str(input('Digite o nome do aluno: ')).title().strip()
    for n in alunos:
        if aluno in n[0]:
            print('='*40)
            print(f'{"Dados do aluno":^40}')
            print(f'Nome: {n[0]} | Média: {n[3]}')
            print('='*40)

            resp = str(input('Deseja ver as notas? [S/N] ')).upper().strip()
            if resp == 'S':
                print('='*40)
                print(f'Primeira nota: {n[1]} | Segunda nota: {n[2]}')
                print('='*40)

                def menu2():
                    print('A) EDITAR AS NOTAS DO ALUNO')
                    print('B) EXCUIR CADASTRO DO ALUNO')
                    print('C) VOLTAR PARA MENU INÍCIAL')
                    print('=' * 40)
                    resp = str(input('Escolha a opção desejada: ')).upper().strip()
                    if resp == 'A':
                        resp = str(input('Qual nota deseja editar? [1/2]: '))
                        if resp == '1':
                            n[1] = int(input('Primeira nota: '))
                            n[3] = (n[1] + n[2]) / 2
                            print('Nota cadastrada com sucesso!')
                            return menu2()
                        elif resp == '2':
                            n[2] = int(input('Segunda nota: '))
                            n[3] = (n[1] + n[2]) / 2
                            print('Nota cadastrada com sucesso!')
                            return menu2()

                    elif resp == 'B':
                        del alunos[alunos.index(n)]
                        print('Aluno escluido com sucesso!')
                        menu()
                    elif resp == 'C':
                        menu()
                    else:
                        print('\033[30mAtenção! \033[31mDados invalidos, digite corretamente.\033[m')
                        return menu2()
                menu2()
            else:
                menu()
    else:
        print(f'O aluno {aluno} não está cadastrado.')
        confirmacao('Deseja cadastrá-lo? [S/N]: ', cadastro, menu)

def confirmacao(txt, txt1, txt2):
    resp = str(input(txt)).upper().strip()
    if resp == 'S':
        return txt1()
    elif resp == 'N':
        return txt2()
    else:
        print('\033[30mAtenção! \033[31mDados invalidos, digite corretamente.\033[m')
        return confirmacao(txt, txt1, txt2)

def menu():
    print('='*40)
    print(f'\033[33m{"DADOS DOS ALUNOS":^40}\033[m')
    print('='*40)
    print('A) Digitar o nome do aluno')
    print('B) Pesquisar nomes cadastrados')
    print('='*40)
    opcao = str(input('Escolha a opção desejada: [A/B]: ')).upper().strip()[0]

    if opcao == 'A':
        nomes()
    elif opcao == 'B':
        pesquisa()
    else:
        print('\033[30mAtenção! \033[31mDados invalidos, digite corretamente.\033[m')
        return menu()

# Início do programa;
inicio()

# TESTE
'''alunos = [['darlan', 8, 9, 8.5], ['carol', 7, 7, 7], ['davi', 10, 10, 10]]

nomes = []
while True:
    nome = str(input('Nome: '))
    for c in alunos:
        if nome in c[0]:
            print(f'Nome: {c[0]} | Primeira nota: {c[1]} | Segunda nota: {c[3]}')

            resp = str(input('Deseja apagar algum dado: '))
            if resp == 's':
                print(alunos.index(c))
                #alunos[alunos.index(c)].clear()
                del alunos[alunos.index(c)]

    print(alunos)'''
# ================ ANÁLISE DO CÓDIGO ==================================================================================
'''
Em comparação os códigos ficaram muito similares, a unica parte que me chamou atenção foi ele ter feito variáveis
simples senrem jogadas para dentro da lista usando um [] com virgula separando, enquanto a minha já foi sendo lançada
dentro da lista. No meu caso a vantagem é que as notas ficaram separadas, enquanto a dele ficou junta. Mas isso é
relativo, uma vez que depende do objetivo, e qualquer uma das opções podem ser acessadas, juntas ou separadas.

Já sobre o programa aprimorado, sem dúvida meu código ficou muito melhor uma vez que é possível permenecer nele em um
loop infinito fazendo cadastro, consulta, alteração e até excluindo os dados. Inclusive esse ponto foi muito importante
o aprendizado, já que foi bem complexo chegar a essa solução corrrigindo as falahas de um clear().

Outros pontos que ficaram muito bons, foi ter feito uma função dentro de uma linha de código que permite ser aceeada
estando na linha, ou fora dela. E ter feito uma função editavel podendo ser usada em varios itens diferentes apenas
trocando o txt.
'''
# ================ MODELO CURSO EM VIDEO ==============================================================================
# PROGRAMA
'''ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resp= str(input('Deseja continuar? [S/N]: '))
    if resp in 'nN':
        break

print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')'''
