'''
DESAFIO 056

Desenvolva um programa que LEIA O NOME, IDADE E SEXO de 4 PESSOAS.
No final do programa mostre:

# A MÉDIA DE IDADE DO GRUPO;
# QUAL É O NOME DO HOMEM MAIS VELHO;
# QUANTAS MULHERES TEM MENOS DE 20 ANOS;

'''

# ==================== MELHOR OPÇÃO DE CÓDIGO =======================================================

media = 0
contador = 0
id_homem = 0

homem = ''
homem2 = ''

for c in range(1, 5):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(c))).upper().strip()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? [M/F]: ')).upper().strip()
    media += idade /4
    if sexo == 'M':
        if idade > id_homem:
            id_homem = idade
            homem = nome
        if id_homem == idade and nome != homem:
            homem2 = nome

    elif sexo == 'F':
        if idade < 20:
            contador += 1
print('=-'*60)
print('A media de idade do grupo é {} anos.'.format(media))

if homem == '':
    print('Não houve nenhum homem listado no grupo.')
elif homem2 == '':
    print('O nome do homem mais velho do grupo é {} e sua idade é {} anos.'.format(homem, id_homem))
else:
    print('Duas pessoas tiverem a mesma idade {} anos. E são os mais velhos do grupo: {} e {}.'.format(id_homem, homem, homem2))
if contador == 1:
    print('A quantidade de mulheres no grupo abaixo dos 20 anos foi {} pessoa.'.format(contador))
elif contador > 1:
    print('A quantidade de mulheres no grupo abaixo dos 20 anos foram {} pessoas.'.format(contador))
elif contador == 0:
    print('Não houve nenhuma mulher listada abaixo dos 20 anos.')

# ===================== OPÇÃO MANUAL SEM O USO DO LAÇO ==================================================

'''
n1 = ''
n2 = ''
n3 = ''
n4 = ''
id1 = 0
id2 = 0
id3 = 0
id4 = 0
s1 = ''
s2 = ''
s3 = ''
s4 = ''

media = 0

h1 = ''

m1 = ''
hv = 0

contador = 0
for c in range(1):
    nome = str(input('Informe o nome da {}ª pessoa: '.format(c+1))).upper().strip()
    idade = int(input('Sua idade: '))
    sexo = str(input('Qual o seu sexo: ')).upper().strip()
    n1 += nome
    id1 += idade
    s1 += sexo
    if sexo == 'mas':
        if idade > hv:
            hv = idade
            h1 = nome

    elif sexo == 'fem':
        m1 = nome
        if idade < 20:
            contador += 1
    for c in range(1):
        nome = str(input('Informe o nome da {}ª pessoa: '.format(c+2))).upper().strip()

        idade = int(input('Sua idade: '))

        sexo = str(input('Qual o seu sexo: ')).upper().strip()
        n2 += nome
        id2 += idade
        s2 += sexo
        if sexo == 'mas':
            if idade > hv:
                hv = idade
                h1 = nome
        elif sexo == 'fem':
            m1 = nome
            if idade < 20:
                contador += 1

        for c in range(1):
            nome = str(input('Informe o nome da {}ª pessoa: '.format(c+3))).upper().strip()

            idade = int(input('A sua idade: '))

            sexo = str(input('Qual o seu sexo: '))
            n3 += nome
            id3 += idade
            s3 += sexo
            if sexo == 'mas':
                if idade > hv:
                    hv = idade
                    h1 = nome

            elif sexo == 'fem':
                m1 = nome
                if idade < 20:
                    contador += 1

            for c in range(1):
                nome = str(input('Informe o nomeda {}ª pessoa: '.format(c+4))).upper().strip()

                idade = int(input('Sua idade: '))

                sexo = str(input('Qual o seu sexo: '))
                n4 += nome
                id4 += idade
                s4 += sexo
                if sexo == 'mas':
                    if idade > hv:
                        hv = idade
                        h1 = nome

                elif sexo == 'fem':
                    m1 = nome
                    if idade < 20:
                        contador += 1

media = (id1 + id2 + id3 + id4) /4

print('A média de idade do grupo é {}'.format(media))
if h1 == '':
    print('Nenhum homem foi citado na lista')
else:
    print('O nome do homem mais valho do grupo foi {} e a sua idade é {}'.format(h1, hv))
if contador > 0:
    print('O número de mulheres abaixo dos 20 anos é {}'.format(contador))
else:
    print('Não houve nenhuma mulher abaixo dos 20 anos.')
'''
