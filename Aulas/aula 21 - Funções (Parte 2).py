'''
AULA 21 - FUNÇÕES (PARTE 2)

>> INTERACTIVE HELP:
Ajuda interativa, é um recurso de documentação para consulta de todas as funções da linguagem.
A forma de acesso é com a função help()

Você pode acessar de duas formas:

Pelo Python Console digitando help() e depois digitando o comando que vc quer ter
informações, para sair basta digitar quit.

Outra forma é campo do código você digita help(len) ou hel(print) ou help(def)... ao executar o programa ele vai te
mostrar as informações do comando desejado.
-----------------------------------------------------------------------------------------------------------------------
>> DOCSTRINGS:
É basicamente um manual da função ou comando, assim como a ajuda interativa. Porem para uma função criada essa
documentação não existe. Daí a necessidade de criar uma docstring.

Imagine uma função:
def linha(txt):
    print('=' *30)
    print(txt)
    print('=' *30)

Um programador que está tendo um primeiro contato com o código, pode não entender o funcionamento da função. Assim, posso
criar uma docstring para explicar o seu funcionamento.
-----------------------------------------------------------------------------------------------------------------------
>> PARÂMETROS OPCIONAIS:
Parâmetros opcionais é a forma para que você ao definir uma determinada quantidade de parâmetros não precise ficar
limitado a quantidade estipulada, podendo usar menos parâmetros.

(Lembrando que para um exemplo aonde não sei quantos valores vou usar, a tecnica seria de MULTIPLOS PARÂMETROS).

Exemplo:
def somar(a, b, c):
    s = a + b + c
    print(f'A soma vale {s}')

soma(3, 2, 5)
Nesse exemplo como foram definidos 3 parâmetros eu tenho que obrigatoriamente inserir 3 valores para o programa funcionar.
Para resolver esse problema eu poderia colocar ao lado de cada parâmetro um =0, assim caso o valor não fosse inserido,
o parâmetro receberia o valor 0.
-----------------------------------------------------------------------------------------------------------------------
>> ESCOPO DE VARIÁVEIS:
Escopo de variável é a definição de onde a variável vai existir e aonde não vai existir.

Existe a variável Global; aquela que funciona em todos os lugares do código. Ela funciona no código principal ou dentro
de alguma função.

Existe a variável Local; essa quando definida dentro de uma função, mesmo que exista outra variável como o mesmo nome
em outro lugar, ela será independente, porem, só funciona no local em que ela foi definida.
-----------------------------------------------------------------------------------------------------------------------
>> RETORNO DE RESULTADOS:
No Python as funções pode ou não retornar um valor. Para retornar basta digitar return.
Essa função tem vários recursos e usos diferentes. Você pode retornar para uma função diferente ou até mesmo, retornar
para um resultado dentro da propria função.
'''
def linha(txt):
    print()
    print(f'{txt:^60}')
    print('='*60)

# ================ INTERACTIVE HELP ===================================================================================
linha('INTERACTIVE HELP')
print(input.__doc__)
help(input)
# ================ DOCSTRINGS =========================================================================================
linha('DOCSTRINGS')
def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: Início da contagem. Ex: i = 0
    :param f: Fim da contagem. Ex: f = 100
    :param p: Passo da contagem. Ex: p = 10
    :return: Sem retono
    -->Assim ele vai fazer uma contagem de 0 a 100 pulando de 10 em 10.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)
contador(0, 100, 10)
# ================ ARGUMENTOS OPCIONAIS ===============================================================================
linha('PARÂMETROS OPCIONAIS')
def somar(a, b, c):
    s = a + b + c
    print(f'A soma vale {s}')
    
    
somar(3, 2, 5)
#Se eu colocar soma(3, 2) o programa daria erro por faltar um valor para completar os 3 parâmetros.
print('=' *30)
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(10)
somar(10, 20)
somar(10, 20, 30)
#Agora não importa quantos valores eu informo (desde que não ultrapasse os parâmetros), o valor que faltar recebe 0.
somar(b=30, a=2)
#Também posso definir o valor do parâmetro

#O mesmo principio funciona com textos.
def l(msg='', msg2='', msg3=''):
    print(msg)
    print(msg2)
    print(msg3)

l(msg3='='*30, msg2='TEXTE COM TEXTO')
# ================ ESCOPO DE VARIÁVEIS ================================================================================
linha('ESCOPO DE VARIÁVEL')
#Escopo de variável é a definição do local aonde a variável existe e aonde deixa de existir.
def teste():
    #Programa Local;
    print('PROGRAMA LOCAL')
    print('-' *30)
    x = 8
    print(f'No programa Local, n vale {n}')
    print(f'No programa Local, x vale {x}') #Como no programa local tem uma variável X definida, ele não mostra a global

#Programa Global;
n = 2
x = 10
teste()
print('PROGRAMA LOCAL')
print('-'*30)
print(f'No programa Global, n vale {n}')
print(f'No programa Global, x vale {x}')
print('-' *30)
def teste(num):
    global a, b, c #Ao colocar essa função, as variáveis locais passaram ser globais
    a = 8
    b = num + 4 #NUM é o valor de A Global
    c = 2
    print(f'No programa Local, A vale {a}')
    print(f'No programa Local, B vale {b}')
    print(f'No programa local, C vale {c}')

print('PROGRAMA GLOBAL')
print('-' *30)
a = b = c = 0
a = 5
print(f'No programa Global, A vale {a}')
print(f'No programa Global, B vale {b}')
print(f'No programa Global, C vale {c}')

print()

print('PROGRAMA LOCAL')
print('-' *30)
teste(a) #O valor de A foi passado para o parâmetro NUM
print()
print('NA SEGUNDA CHAMADA OS RESULTADOS MUDAM')
print('=' *30)
print(f'No programa Global, A vale {a}')
print(f'No programa Global, B vale {b}')
print(f'No programa Global, C vale {c}')

print()

print('PROGRAMA LOCAL')
print('-' *30)
teste(a)
# ================ RETORNO DE RESULTADOS ==============================================================================
linha('RETORNO DE RESULTADOS')
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(2, 4, 4)
somar(2, 3)
somar(2)
#Se eu quisesse mostrar os resultados todos juntos. Por ex: As somas valem 10, 5 e 2 - Não daria!!!!!
print('-' *30)
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(2, 4, 4)
r2 = somar(2, 3)
r3 = somar(2)
print(f'As somas valem {r1}, {r2} e {r3}')

print('-' *30)
#Exemplo com resultado Logico;
def par(n=0):
    if n % 2 == 0:
        #return 'Verdadeiro'
        return True
    else:
        #return 'Falso'
        return False

num = int(input('Digite um número: '))
#print(f'O número digitado é Par? {par(num)}')
if par(num):
    print('É Par!')
else:
    print('É Ímpar!')
