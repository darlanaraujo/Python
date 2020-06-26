'''
DESAFIO 004

Faça um program que leia algo e mostre na tela o SEU TIPO PRIMITIVO
E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

Usando as funções .is
'''
# ============= CÓDIGO BASE ===========================================================================================
txt = str(input('Digite algo a sua escolha [Letra ou número]: '))
print(f'Você digitou {txt} a sua classe é {type(txt)}, segue abaixo as suas caracteristicas:')
print('-='*30)
print(f'    --> é alfanumérico (número e/ou texto): {txt.isalnum()}')
print(f'    --> é alfabeto (apenas texto): {txt.isalpha()}')
print(f'    --> é {txt.isascii()}')
print(f'    --> é decimal (apenas número): {txt.isdecimal()}')
print(f'    --> é um digito apenas númerico: {txt.isdigit()}')
print(f'    --> é um texto sem espaço: {txt.isidentifier()}')
print(f'    --> é um texto com todas letras minusculas: {txt.islower()}')
print(f'    --> é apenas espaço em branco: {txt.isspace()}')
print(f'    --> é um conteúdo imprimivel (vazio ou texto/números): {txt.isprintable()}')
print(f'    --> é um texto com a 1ª letra maiúscula: {txt.istitle()}')
print(f'    --> é um texto com todas letras maiúsculas: {txt.isupper()}')

