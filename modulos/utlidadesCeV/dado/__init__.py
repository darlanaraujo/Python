# =============== CÓDIGO BASE =========================================================================================
'''def leiadinheiro(msg):
    from modulos.utlidadesCeV import moeda
    ok = False
    valor = 0
    while True:
        n = str(input(msg))

        if ',' in n:
            n = n.replace(',', '.')
            valor = float(n)
            ok = True

        elif n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print(f'\033[31mERRO! \033[33m{n.upper()}\033[31m é um dado inválido. Digite apenas números!\033[m')
            print('-='*30)

        if ok:
            break

    return moeda.resumo(valor, 35, 22)'''

# ============== ANÁLISE DO CÓDIGO ====================================================================================
'''
ex112 - Meu código cumpriu (em parte) com o enunciado, porém, não conseguia resolver o problema de mostrar a formatação
do número com , ao invés de . - Outra coisa é que por está usando isnumeric meu código não aceitava quando a pessoa
digitava um número com . ele só aceita se usar a virgula.

Tudo isso é resolvido no código do curso, justamente por usar um recurso diferente, primeiro que ele continua usando
o pacote dado na linha do código principal e não dentro do módulo como eu fiz. Outra coisa é que o tratamento dos erros
que ele usou dentro do módulo foi melhor e mais limpo.

No entando o programa dele também não está completo, pois se usar um w3 por exemplo, o programa dele da erro! Já o meu
aceita. Mas se colocar no meu um 450.50 o meu da erro, e o dele aceita.
'''
# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg): # A msg é o texto 'Digite um número'
    ok = False # Essa variável é apenas para iniciar ou parar o laço.
    valor = 0
    while True:
        n = str(input(msg)) # Aqui ele inseriu a mensagem na variavel n como se fosse n=str(input('Digite um número'))
        if n.isnumeric(): # Aqui ele vai verificar se n é um número.
            valor = int(n) # Sendo um número, n recebe o valor que foi digitado em n
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor # Sem esse retorno, o valor que foi inserido no laço não é validado.