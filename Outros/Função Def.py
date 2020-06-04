# Definição de linhas simples
def linhas():
    print('|','='*50,'|')


linhas()

# Definição de cabeçalho com texto personalizado
def cabecalho(txt):
    print(f'|{"="*50}|')
    print(f'|{txt:^50}|')
    print(f'|{"="*50}|')


cabecalho('BANCO 24 HORAS')

# Definição de erro

def erro(txt):
    while True:
        retur = str(input(txt)).upper().strip()[0]
        if retur == 'S':
            break
        if retur == 'N':
            break
        else:
            print('OPÇÃO INVÁLIDA! DIGITE CORRETAMENTE.')


erro('VOLTAR AO MENU PRINCIPAL? [S/N]: ')