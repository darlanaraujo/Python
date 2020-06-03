'''
DESAFIO 069

Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá PERGUNTAR SE O USUÁRIO
QUER ou NÃO CONTINUAR.

No final mostre:

A) Quantas pessoas tem MAIS de 18 ANOS.
B) Quantos HOMENS foram cadastrados.
C) Quantas MULHERES tem MENOS de 20 ANOS.
'''
# =============== VARIAVEIS GLOBAIS =========================================================
homens = mulheres = maior = cont = 0

# =============== LAYOUT DO PROGRAMA ========================================================
print(f'|{"="*40}|')
print(f'|\033[33m{"CADASTRO DO CLIENTE":^40}\033[m|')
print(f'|{"="*40}|')

# =============== INÍCIO DO PROGRAMA ========================================================
while True:
    idade = int(input('| \033[30mInforme a idade:\033[m '))
    sexo = str(input('| \033[30mInforme o sexo:\033[m ')).upper().strip()[0]
    cont += 1
    print(f'|{"="*40}|')
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulheres += 1
    if idade > 18:
        maior += 1
    while True:
        resp = str(input('| \033[33mContinuar cadastrando? [S/N]:\033[m ')).upper().strip()[0]
        print(f'|{"="*40}|')
        if resp == 'S':
            break
        elif resp == 'N':
            break
        else:
            print(f'|\033[31m{"ATENÇÃO! DADOS INVALIDOS.":^40}\033[m|')
    if resp == 'N':
        break


# =============== RODAPÉ DO PROGRAMA =======================================================
print(f'|\033[30m{"FIM DO CADASTRO":^40}\033[m|')
print(f'|{"="*40}|')
print()

# =============== CONCLUSÃO DO PROGRAMA =====================================================

#Layout
print(f'\033[30m|{"#"*70}|')
print(f'|{"#"*70}|')
print(f'|\033[33m{"RELATÓRIO DE CADASTROS":^70}\033[30m|')
print(f'|{"="*70}|')

#Conteudo
if maior > 1:
    print(f'| Entre os cadastros \033[33m{maior}\033[30m pessoas tem \033[33mMAIS DE 18 ANOS.\033[30m')
else:
    print(f'| Entre os cadastros \033[33m{maior}\033[30m pessoa tem \033[33mMAIS DE 18 ANOS.\033[30m')
if homens > 1:
    print(f'| Foram cadastrados \033[33m{homens} HOMENS.\033[30m')
else:
    print(f'| Foi cadastrado \033[33m{homens} HOMEN.\033[30m')
if mulheres > 1:
    print(f'| Foram cadastradas \033[33m{mulheres}\033[30m mulheres com \033[33mMENOS DE 20 ANOS.\033[30m')
else:
    print(f'| Foi cadastrada \033[33m{mulheres}\033[30m mulhere com \033[33mMENOS DE 20 ANOS.\033[30m')

#Layout
print(f'|{"#"*70}|')
print(f'|{"#"*70}|')