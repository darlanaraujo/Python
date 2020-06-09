'''
AULA 20 - Funções (Parte 1) - FUNÇÃO DEF = Definição de função

A criação de uma função é um recurso para utilização em rotinas. Sempre que precisar executar uma tarefa repeditamente.
Porem ele é mais que isso, podendo ser usado para fazer com que a linha do programa pule de um lugar para o outro sem
seguir uma ordem.

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
def titulo(txt):
    print('-'*30)
    print(f'{txt:^30}')
    print('-'*30)

titulo('PERSONALIZADO')