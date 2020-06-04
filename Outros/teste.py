#Pergunta 1
def pergunta1 (euros_pergunta):
    print('Qual era o codnome do rei portugês D.Afonso II?')
    print('A) O conquistador')
    print('B) Oventuroso')
    print('C) O africano')
    print('D) O gordo')

    a = raw_input ('Qual a opção correta:')

    if (a == 'd'):
        return euros_pergunta
    else:
        return 0

#####################################################################################

#Inicio

print('Bem-vindo(a) ao jogo de Perguntas e Resposta 2.0')

lista_niveis = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 150000, 250000, 500000, 1000000]

print('Níveis dos Prémios')

for index in range(0,len(lista_niveis),1):
    print('Níveis:'),lista_niveis[index], '$'

inicio = raw_input ('Deseja iniciar o jogo (s/n) ?')

index = 0

while (inicio == 's' or inicio == 'S'):

#Pergunta 1

    resultado = pergunta1(lista_niveis[index])
    if resultado == 0:
        print('Final do jogo: Você ganhou R$ 0')
        break
    else:
        print('Parabéns! Você acaba de ganhar R$ 100,00')

    cont = raw_input ('Deseja continuar jogando (s/n)? ')
    if (cont == 'n' or cont == 'N'):
        break

#Fim do jogo

print('Fim do jogo')