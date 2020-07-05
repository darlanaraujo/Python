# ================ CÓDIGO BASE ========================================================================================
'''def aumentar(n, p, form=False):
    """
        --> A função recebe o valor do parâmetro e retorna o resultado aumentando o valor da porcentagem.
    :param n: Valor em reais informado pelo usuário
    :param p: Valor da porcentagem que aumentará o valor final
    :param form: Se o usuário colocar como parâmetro (True) a função personaliza o código como valor monetário
    :return: Retorna o valor com o resultado do calculo.
    """
    porc = n / 100 * p
    soma = n + porc
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def diminuir(n, p, form=False):
    """
        --> A função recebe o valor do parâmetro e retorna o resultado diminuindo o valor da porcentagem.
    :param n: Valor em reais informado pelo usuário
    :param p: Valor da porcentagem que diminui o valor final
    :param form: Se o usuário colocar como parâmetro (True) a função personaliza o código como valor monetário
    :return: Retorna o valor com o resultado do calculo.
    """
    porc = n / 100 * p
    soma = n - porc
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def dobro(n, form=False):
    """
        --> A função recebe o valor do parâmetro e retorna o dobro do valor no resultado.
    :param n: Valor em reais informado pelo usuário
    :param form: Se o usuário colocar como parâmetro (True) a função personaliza o código como valor monetário
    :return: Retorna o valor com o resultado do calculo.
    """
    soma = n * 2
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def metade(n, form=False):
    """
        --> A função recebe o valor do parâmetro e retorna o resultado com a metade do valor.
    :param n: Valor em reais informado pelo usuário
    :param form: Se o usuário colocar como parâmetro (True) a função personaliza o código como valor monetário
    :return: Retorna o valor com o resultado do calculo.
    """
    soma = n / 2
    if form:
        soma = f'R$ {soma:.2f}'
    return soma


def moeda(n):
    """
        --> A função recebe o valor do parâmetro e converte os números para valor monetário.
    :param n: Valor em reais informado pelo usuário
    :return: Retorna o valor formatado em moeda real.
    """
    n = f'R$ {n:.2f}'
    return n


def resumo(v, a, d):
    """
        --> A função recebe o valor do parâmetro e retorna o resultado simplificando o código do programa principal
        uma vez que lá, basta fazer a chamada da função e o resultado da função está definido aqui.
    :param v: Valor em reais informado pelo usuário
    :param a: Valor da porcentagem para aumento do valor final
    :param d: Valor da porcentagem para desconto do valor final
    :return: Retorna o resultado final com todas as formatações definidas pelas funções.
    """
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'{"Preço analisado:":<22} {moeda(v)}')
    print(f'{"Dobro do preço:":<22} {moeda(dobro(v))}')
    print(f'{"Metade do preço:":<22} {moeda(metade(v))}')
    print(f'{a}{"% de aumento:":<20} {moeda(aumentar(v, a))}')
    print(f'{d}{"% de redução:":<20} {moeda(diminuir(v, d))}')
    print('-'*35)'''

# =================== ANÁLISE DO CÓDIGO ===============================================================================
'''
ex107 - O resultado dos códigos são os mesmos, o ponto mais destacado é a importancia de usar bem as palavras que
definem os parâmetros para não dificultar o entendimento final. O código do curso usou melhor isso, deixando claro a
identificação desses parâmetros. Exemplo: preço e taxa... ao invés de usar a, b, c...

ex108 - A criação da função moeda, o código do curso usou um recurso muito bom que foi o replace, aonde ele subistitui
o . po , - dessa forma o resultado final fica muito melhor. Outro ponto importante foi ele ter padronizado os parâmetros
para receber 0 caso o usuário não passe nenhum.

ex109 - O código do curso usou o recurso de condição para direcionar para a função moeda usando o código em apenas
uma linha, assim além de funcional o código fica limpo e curto. diferente do meu que recriei dentro da função a
formatação dos valores, e com isso a função moeda não seria usada!

ex110 - Novamente o código do curso ficou melhor. Nessa aula foi mostrado dois recursos novos. Após o texto você pode
usar .center() para centralizar o texto. E ao usar \t você cria uma tabulação automática organizando o texto. Além
disso, o código do curso fez uso do parâmetro formato, enquanto o meu eu tive que apontar manualmente para a função
moeda.

ex111 -  
'''
# =================== CÓDIGO CURSO EM VÍDEO ===========================================================================
def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res) # Aqui ele está direcionando para função moeda, que formata o texto.
    #Ou seja! Retorne res se o formato for falso. Senão retorne a função moeda(res) com o res dentro.


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res) # Aqui ele está direcionando para função moeda, que formata o texto.


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res) # Aqui ele está direcionando para função moeda, que formata o texto.
    # Retorne res se formato não for verdade (ou não tiver = False). Senão (se tiver = True) retorne moeda(res).


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res) # Aqui ele está direcionando para função moeda, que formata o texto.


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)