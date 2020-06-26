'''
DESAFIO 002

Crie um script que leia O DIA, MÊS E ANO DE NASCIMENTO de uma pessoa
e mostre uma mensagem com a data formatada.
'''
# ============ CÓDIGO BASE ============================================================================================
nome = str(input('Qual o seu nome: ')).title().strip()
print(f'Olá {nome}, informe abaixo o dia, mês e ano do seu nascimento!')
dia = int(input('Informe o dia: '))
mes = str(input('Qual o mês: '))
ano = int(input('Por fim, qual o ano: '))

print('-='*30)
print(f'Seu nome é {nome}, e a data de nascimento é {dia}/{mes}/{ano}')