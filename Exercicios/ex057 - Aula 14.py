'''
DESAFIO 057 - AULA 14

Faça um programa que LEIA O SEXO DE UMA PESSOA, mas só ACEITE OS VALORES 'M' ou 'F'.
Caso esteja ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE até ter um valor CORRETO.
'''

# ===================== FORMA CORRETA DE USO DO LAÇO ===================================

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('\033[31mATENÇÃO! Dados inválidos.\033[m')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

print('Sexo \033[33m{}\033[m registrado com sucesso.'.format(sexo))

# ===================== INÍCIO DO CÓDIGO ===============================================
'''sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0] #Fateamento para pegar só a primeira letra digitada
    if sexo != 'M' and sexo != 'F':
        print('Você digitou um valor errado!')
print('FIM')

# ====================== APLICAÇÃO DO CÓDIGO EM UM PROGRAMA =============================

#Programa de cadastro

# ================== VARIÁVEL GLOBAL ===================================================
sexo = ''

# ================== CADASTRO DO CLIENTE ===============================================
nome = str(input('Nome do Cliente: ')).upper().strip()
idade = int(input('Idade: '))
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Valor digitado incorreto! As opções são [M/F]')
print()
print('=-'*20)
print('Cadastro concluido.')

# =================== FIM DO PROGRAMA ==================================================
'''
