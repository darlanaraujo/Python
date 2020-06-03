#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerer espaços)
#Quantas letras tem o primeiro nome.

print('{:=^40}'.format('EXERCICIO 22'))
nome=input('Digite o seu nome completo? ').strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' ')) #Essa função elimina os espaços entre as palavras
#Abaixo temos duas opções de leitura da quantidade de caracteres
print(len(nome.split()[0]))
print(nome.find(' ')) #Essa opção fica mais facil de escrever uma vez que ela elimina a partir do primero espaço e vc não precisa fatiar o texto com a função split