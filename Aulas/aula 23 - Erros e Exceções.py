'''
AULA 23 - TRATAMENTO DE ERROS E EXCEÇÕES

O ERRO mais comum é sintaxe - Quando se erra uma palavra.
Exemplo: primt(x) / input(('texto) / else;

Mas os erros mais cometidos são erros de significado (erro semantico).

Nesse caso o nome usado é EXCEÇÃO
Exemplo: print(x) # Nesse caso mesmo que o comendo esteja correto, mas, por não ter definido a variável o programa
daria erro. NameError.

Esse tipo de EXCEÇÃO pode ocorrer de várias maneiras, outro exemplo: n = int(input('Digite um número: '))
O código está certo, porém, se o usuário digitar um texto ao invés de número, o programa vai dar erro. ValuerError.
'''
# ============== ERRO DE SINTAXE ======================================================================================
# Esse é um erro de sintaxe, aonde o comando foi digitado errado.
'''primt(x) # comando pint digitado errado.
num = int(input(('Digite um número: ')) # comando com excesso de parenteses

# ============== EXCEÇÕES =============================================================================================
# Exceções de erros. Quando o comando está certo, mas a execução da erro.

print(x) #Ainda que o comando esteja correto, não foi definido a variável X. NameError

n = int(input('Digite um número: ')) #O comando está correto, mas se o usuário digitar W. ValuerError.

a = 8
b = 0
r = a / b #Esse comando daria erro, devido ao divisor 0. ZeroDivisionError

s = 2 / '2' #Esse comando daria erro uma vez que são tipos diferentes (numeral x texto). TypeError

lst = [9, 2, 4]
print(lst[3]) #Esse comando daria erro, uma vez que a lista vai de 0 a 2. IndexError

# Outras Exceções: KeyError, EOFError, KeyboardInterrupt, OSError, MemoryError, ConnectionError, RuntimeError
'''
# ============== RETORNO QUANDO UM ERRO OU EXCEÇÃO É ENCONTRADA =======================================================

'''
Traceback (most recent call last):
  File "C:/Users/Visa Remoções/Desktop/Darlan/Python/Outros/teste 2.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
'''

# ============== TRATANDO ERROS E EXCEÇÕES ============================================================================

'''
No Python e em várias linguagens de programação existe um comando para tratamento de erros e exceções. Com ele você
"TENTA" executar um comando, e caso não funcione, ela fara outra coisa.

OS COMANDOS SÃO:
try:
    Aqui colocamos a operação.
except:
    Aqui colocamos o comando que acontece caso haja uma falha.
else:
    Aqui colocamos a solução caso o try: funcione.
finally:
    Aqui colocamos um comando ou msg para encerramento da ação.
    
O comando try: é para tentar executar algo
O comando except: é caso dê algum problema e ele pode mostrar outro resultado ou ação.
Ao colocar o else: com a solução caso o programa não dê erro.
O finally permite da um encerramento ao comando independente que dê certo ou errado.

Isso faz com que mesmo tendo algum erro, ao invés de interromper o programa e aparecer a mensagem vermelha. O programa
vai continuar funcionando (se estiver em um loop) e o programador pode colocar uma mensagem personalizada.

Outra coisa que podemos fazer é usar o Exception as (variavel): e abaixo podemos descrever o tipo do erro.
__class__ /
'''

# AULA PRÁTICA
try:
    a = int(input('Denominador: '))
    b = int(input('Divisor: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erros:
    print(f'O erro encontrado foi {erros.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado.')

# MAIS EXEMPLOS:

try:
    a = int(input('Denominador: '))
    b = int(input('Divisor: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado.')