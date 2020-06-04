'''
FUNÇÃO RETURN JUNTAMENTE COM A FUNÇÃO DEF

A função return retorna um valor/ informação;

E se estamos retornando algo, alguma coisa precisa receber esse retorno.
Quem vai 'receber' o 'return' será a variável 'nome'.
'''

# ============ EXEMPLO DE USO DAS FUNÇÕES =============================================
'''
Crie um programa em Python que tenha a função soma(x,y) que recebe dois números e
retorna o valor da soma deles.
'''

'''def soma(x,y):
    resultado = x + y
    return resultado

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

resposta = soma(a,b)

print('Resposta: {}'.format(resposta))'''

# ================ EXEMPLO USANDO STRING =========================================
'''
Crie um programa em Python que peça o nome e o sobrenome de uma pessoa, depois
exiba na tela a mensagem "Olá sobrenome, nome"
'''

'''def invert(nome, sobrenome):
    nome_inverso = sobrenome + ', ' + nome
    return nome_inverso

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))

#teste = sobrenome + ', ' + nome
invertido = invert(nome, sobrenome)

print('Olá, {}'.format(invertido))'''

# =============== EXEMPLO COM BOOLEANOS ===================================================
'''
Crie um programa em Python que diz se o número inserido pelo usuário é par ou ímpar.
Ele deve fazer isso através de uma função que recebe o inteiro e retorna True ou False.
'''
'''def par_impar(x):
    if x % 2 == 0:
        return True
    else:
        return False

while True:
    n1 = int(input('Digite um número: '))
    if par_impar(n1):
        print('O número é par!')
    else:
        print('O número é impar!')'''

# ============== UMA APLICAÇÃO MELHOR PARA STRING =========================================
'''def nome(x):
    if x == 'Darlan':
        return True
    else:
        return False

while True:
    resposta = str(input('Qual o meu nome? ')).capitalize()
    if nome(resposta):
        print('Correto!')
        break
    else:
        print('Você errou!')'''

# ================= COMO RETORNAR MAIS DE UM VALOR ==================================

'''def cadastro():
    nome = str(input('Informe o nome: ')).upper().strip()
    idade = int(input('Informe a idade: '))

    return nome, idade

print('INÍCIO DO CADASTRO:')
nome, idade = cadastro()

print()
print('CADASTRO REALIZADO COM SUCESSO!')
print('Seu nome é {}, e sua idade é {}'.format(nome, idade))'''

# ================= COMANDO DEFINIÇÃO PARA PENSAGEM DE ERRO ==================================
def alerta():
    erro = '\033[31mATENÇÃO! Digite um valor correto. \033[33m[S/N]\033[m'

    return erro

while True:
    resposta = str(input('Deseja continuar o jogo? [S/N]: ')).upper()
    if resposta == 'S':
        print('OK')
    elif resposta == 'N':
        print('Negação')
    else:
        print(alerta())