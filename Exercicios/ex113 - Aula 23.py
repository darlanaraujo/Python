'''
DESAFIO 113

Reescreva a função LEIAINT() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função LEIAFLOAT() com a mesma funcionalidade.
'''
# ============== CÓDIGO BASE ==========================================================================================
'''def leiaint(msg):
    try:
        n = str(input(msg)).strip()
        n = int(n)
    except (KeyboardInterrupt):
        print('ERRO! O usuário preferiu não informar os dados.')
        return 0
    except:
        print('\033[31mERRO! Digite um número \033[33m\"inteiro\"\033[31m válido!\033[m')
        return leiaint(msg)
    else:
        return n


def leiafloat(msg):
    try:
        real = str(input(msg)).strip().replace(',', '.')
        real = float(real)
    except KeyboardInterrupt:
        print('ERRO! O usuário preferiu não informar os dados.')
        real = 0
        return real
    except:
        print('\033[31mERRO! Digite um número \033[33m\"real\"\033[31m válido!\033[m')
        return leiafloat(msg)
    else:
        return real


n = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')'''
# ============== CÓDIGO MELHORADO =====================================================================================

# ============== ANÁLISE DO CÓDIGO ====================================================================================

# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue #Esse comando faz com que o programa volte para o while nesse ponto.
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')