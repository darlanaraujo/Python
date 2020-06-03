# Nessa aula vamos aprender sobre comando em análise e trasfrmação de strings
frase = str(input('Digite um texto qualquer: '))
print(frase[1:]) #Ao utilizar [1:] com numeros dentro, você consegue mostrar a letra correspondente ao numero escolhido
print(len(frase))  # Esse comando len mostra a quantidade de caracteres que contem dentro da variável
print(frase.count('a'))  # O comando count('') mostra a quantidade de caracteres selecionada contem dentro da variável
print(frase.find('r'))  # O comando find('') mostra o momento que o determinado caractere começa dentro da variável
print('007' in frase)  # O comando in mostra se o determinado caractere existe dentro da variável
print(frase.replace('Darlan', 'Dan 007'))  # O comando replace substitu um caractere por outro, mas não muda a variável
print(frase.upper())  # O comando upper coloca o texto maisculo
print(frase.lower())  # O comando lower coloca o texto minusculo
print(frase.capitalize()) #O comando capitalize() deixa apenas a primeira letra em maisculo
print(frase.title()) #O comando title() vai colocar o começo de todos os textos em maisculo
print(frase.strip()) #O comando strip() vai remover todos os espaços desnecessários no inicio e fim do texto
print(frase.rstrip()) #O comando rstrip() vai remover os espaços desnecessários do lado direito do texto
print(frase.lstrip()) #O comando lstrip() vai remover os espaços desnecessários do lado esquerdo do texto
print(frase.split()) #O comando split() divide o texto fazendo com que cada parte ocupe uma memória separada
print('-'.join(frase)) #O comando '-'.join junta os textos e os separa usando a caractere dentro das aspas

# PARA JUNTAR 2 PRINT NA MESMA LINHA PODE-SE USAR A FUNÇÃO ABAIXO. OU PARA QUEBRAR UM TEXTO NO MESMO PRINT.
print('Texto 1 na primeira linha.',end=' ')
print('Texto 2 na segunda linha \nTexto 3 na terceira linha usand a quabra.')

# Para quebrar um print em várias linhas sem precisar repetir o print
print('''Texto 1
Texto 2
Texto3''')

# Atualização para uso de variaveis com o Print
nome = 'Darlan'
idade = 35
salario = 987.3
print('Nome: %s, Idade: %d anos.' % (nome, idade)) #Forma antiga Python 2
print('Nome: {}, Idade: {} anos.'.format(nome, idade)) #Forma Python 3
print(f'Nome: {nome}, Idade: {idade} anos.') #Forma aturalizada Python 3.6+

#Exemplo com uma formatação de casas decimais e alinhamento no texto
print(f'Nome: {nome:^20}, Idade: {idade:=^20} anos, e ganha R$ {salario:.2f}')
