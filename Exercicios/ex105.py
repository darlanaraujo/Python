'''
DESAFIO 105

Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber várias notas de alunos e vai retornar um DICIONÁRIO
com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as DOCSTRINGS da função.
'''
# ============ CÓDIGO BASE ============================================================================================
def notas(* num, st=False):
    '''
        --> A função recebe os valores digitados, os coloca em um dicionário e faz um laço para separar os valores,
        mostrando o resultado de Maior Nota, Menor Nota, Média, e (opcional) a situação.
    :param num: Recebe os valores digitados
    :param st: Recebe o comando para mostrar ou não a situação
    :return: Mostra o resultado separando os valores de acordo com as metas
    '''
    alunos = {'Notas': num, 'Situação': st}
    soma = maior = menor = 0
    print(alunos)
    for p, v in enumerate(alunos['Notas']):
        soma += v
        if p == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v

    print(f'A maior nota foi {maior}')
    print(f'A menor nota foi {menor}')
    media = soma / len(alunos['Notas'])
    print(f'A média da turma é {media:.2f} ', end='')
    if st == True:
        if media < 5.9:
            print('\033[31mMédia Baixa!')
        elif media < 7:
            print('\033[33mMédia Razoavel!')
        elif media >= 7:
            print('\033[34mMédia Boa!')


notas(1, 7, 3.5, 9, st=True)

# ============ CÓDIGO MELHORADO =======================================================================================

# ============ ANÁLISE DO CÓDIGO ======================================================================================

# ============ CÓDIGO DO CURSO EM VÍDEO ===============================================================================
