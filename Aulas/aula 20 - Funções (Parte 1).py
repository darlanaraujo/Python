'''
AULA 20 - Funções (Parte 1) - FUNÇÃO DEF = Definição de função

A criação de uma função é um recurso para utilização em rotinas. Sempre que precisar executar uma tarefa repeditamente.
Porem ele é mais que isso, podendo ser usado para fazer com que a linha do programa pule de um lugar para o outro sem
seguir uma ordem.

Exemplo de uma função def;
def soma(a, b):
    s = a + b
    print(s)

soma(4, 6)

def - é a função / soma() - é o nome da função / (a, b) - O que está dentro é o parâmetro
O que vai embaixo é a rotina definida.
soma(4, 6) - A forma de mostrar a função e os números são a definição do parâmetro.
'''
# =============== EXEMPLOS ============================================================================================
def separação(txt):
    print()
    print(f'{txt:^60}')
    print('='*60)

separação('FUNÇÃO MOSTRA LINHA')
# No modelo abaixo vou mostrar uma linha padrão toda vez que eu usar;
def linha():
    print('-'*30)

linha()

separação('FUNÇÃO CABEÇALHO')
# No modelo abaixo vou mostrar um cabeçalho padrão toda vez com as mesmas informações;
def cabecalho():
    print('-'*30)
    print(f'{"TITULO DO PROGRAMA":^30}')
    print('-'*30)

cabecalho()

separação('FUNÇÃO TITULO PERSONALIZADO')
# No modelo abaixo posso fazer um cabeçalho editavel;
def titulo(l1, txt, l2):
    print(l1)
    print(f'{txt:^30}')
    print(l2)

titulo('-'*30,'PERSONALIZADO', '-'*30)

separação('FUNÇÕES PARA CALCULOS')
# Modelo de funções com calculos; Nota: quando defino 2 parâmetros, eu não posso usar nem menos nem mais.
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('='*30)

soma(4, 6) #O conteudo que vai dentro das () é chamado de parâmetro
soma(a=6, b=4) #Outra coisa que posso fazer é definir o valor com o parâmetro.

separação('EMPACOTAMENTO DE PARÂMETRO')
# O empacotamento de função é a possibilidade de vc poder definir quantidades variáveis de parâmetro em uma mesma
# função. Nota: Isso só é possivel fazer no Python, outras liguagens não permitem.
# A forma de dizer para o Python que vc vai variar os parâmetros é usando * antes do nome do parâmetro.
def contador(* num):
    print(f'Recebi o valor de {num} e o tamanho é {len(num)} números')
    for p, valor in enumerate(num):
        print(f'Na {p} encontrei {valor}')

contador(1, 3, 5, 9)
contador(4, 1, 10)
contador(2, 4)

separação('USANDO FUNÇÕES COM LISTAS')
# Abaixo vamos usar uma função para dobrar o valor de uma lista.
valores = [7, 2, 5, 0, 4]
def dobra(lst):
    print(lst)
    pos = 0
    while pos <len(lst):
        valores[pos] *= 2
        pos += 1
    print(lst)

dobra(valores)