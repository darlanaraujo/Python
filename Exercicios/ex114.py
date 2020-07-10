'''
DESAFIO 114

Crie um código em PYTHON que teste se o site PUDIM está acessível pelo computador usado.
'''
# ============== CÓDIGO BASE ==========================================================================================

# ============== CÓDIGO MELHORADO =====================================================================================
def sites(msg):
    from time import sleep
    import urllib.request

    print('=-' * 30)
    print('SISTEMA PARA CONSULTA DE SITE'.center(60))
    print('=-' * 30)

    url = str(input(msg))
    site = f'http://{url}'
    print('=-'*30)
    try:
        acesso = urllib.request.urlopen(site)
    except:
        print(f'\033[31mO Site {site} está fora do ar\033[m')
    else:
        print(f'\033[33mO Site {site} está online!\033[m')
        return acesso
    finally:
        while True:
            print('=-' * 30)
            resp = str(input('Deseja consultar outro site? [S/N]: ')).upper().strip()
            if resp == 'S':
                return sites(msg)
            elif resp == 'N':
                print('=-' * 30)
                print('Finalizando', end='')
                sleep(.5)
                for c in range(1, 5):
                    print('.', end='')
                    sleep(.5)
                print('Volte sempre!')
                break
            else:
                print('=-' * 30)
                print('\033[31mERRO! Digite apenas \033[33mS \033[31mou \033[33mN\033[31m.\033[m')



link = sites('Digite o endereço do site: ')
# ============== ANÁLISE DO CÓDIGO ====================================================================================
'''
Como não conhecia o comando para esse tipo de programa, não consegui fazer o código. Ao ver o código do curso, tentei
aprimora-lo com alguns recursos, como permitir ao usuário que digite o endereço do site a ser pesquisado, e ele pode
fazer varias pesquisas ou sair do programa. 
'''
# ============== CÓDIGO CURSO EM VÍDEO ================================================================================
'''import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim está acessivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())'''