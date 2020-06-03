#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade=str(input('Digite um nome de uma cidade: ')) #Sempre lembrar de utilizar o strip para eliminar os espaços
cidade=cidade.title().strip()
print('A cidade escolhida foi: {}'.format(cidade))
print('A verificação se a cidade começa com o nome Santo é: {}'.format('Santo' in cidade.split()[0]))
#c1=cidade.split()
#print('Santo'in c1[0])