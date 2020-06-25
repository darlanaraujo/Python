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
    """
        --> A função recebe os valores digitados, os coloca em um dicionário e faz um laço para separar os valores,
        mostrando o resultado de Maior Nota, Menor Nota, Média, e (opcional) a situação.
    :param num: Recebe os valores digitados
    :param st: Recebe o comando para mostrar ou não a situação
    :return: Mostra o resultado separando os valores de acordo com as metas
    """
    alunos = {'Notas': num, 'Total de Notas': len(num)}
    soma = maior = menor = 0

    for p, v in enumerate(alunos['Notas']):
        soma += v
        if p == 0:
            maior = menor = v
            alunos['Maior Nota'] = v
            alunos['Menor Nota'] = v
        else:
            if v > maior:
                maior = v
                alunos['Maior Nota'] = maior
            if v < menor:
                menor = v
                alunos['Menor Nota'] = menor

    print(alunos)
    print(f'A maior nota foi {maior}')
    print(f'A menor nota foi {menor}')

    alunos['Media'] = soma / len(alunos['Notas'])
    print(f'A média da turma é {alunos["Media"]:.2f} ', end='')
    if st == True:
        if alunos['Media'] < 5.9:
            return '\033[31mMédia Baixa!'
        elif alunos['Media'] < 7:
            return '\033[33mMédia Razoavel!'
        elif alunos['Media'] >= 7:
            return '\033[34mMédia Boa!'


help(notas)
print(notas(1, 10, 7, 3.5, 9, st=True))

# ============ CÓDIGO MELHORADO =======================================================================================

# ============ ANÁLISE DO CÓDIGO ======================================================================================

# ============ CÓDIGO DO CURSO EM VÍDEO ===============================================================================
def notas(*n, sit=False):
    """
    --> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
help(notas)
resp = notas(3.5, 6, 8, 2, sit=True)
print(resp)