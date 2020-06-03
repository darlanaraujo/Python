'''
AULA 12 - CONDIÇÕES ANINHADAS

Uma condição aninhada é formada pelos comandos abaixo;

if /Que representa a palavra "SE"
elif /Que representa a palavra "SENÂO SE"
else /Que representa a palavra "SENÃO"

Ao utilizar uma condição aninhada eu posso usar quantas vezes for necessário a função "elif"
enquanto a função "if" é usada apenas uma vez no começo. E a função "else" pode ou não ser
usada uma vez no final.
'''

print('Você tem CINCO caminhos para escolher. \n\033[1;30m1º) Para frente\033[m \n\033[1;31m2º) Para traz\033[m \n\033[1;32m3º) Para esquerda\033[m \n\033[33m4º) Para direita\033[m \n\033[1;34m5º) Ficar parado\033[m')
print()
caminho = str(input('O que deseja fazer? ')).lower().strip()
#if 'frente' and 'ir para frente' and 'para frente' in caminho: #Aqui temos uma segunda opção para o mesmo comando.
if caminho == 'frente' or caminho == 'ir para frente' or caminho == 'para frente':
    print('Ok. Vamos seguir em frente!')
#Abaixo uma segunda opção de fazer o mesmo comando usando a função "in"
#elif 'traz' or 'ir' or 'voltar' in caminho: #Dessa forma não importa o que a pessoa digite. Se tiver a palavra selecionada dentro da variável ele vai funcionar.
elif caminho in 'traz , ir volta voltar': #Nesse exemplo a variável vem primeiro e dentro da string pode colocar várias palavras chaves juntas.
#elif caminho == 'traz' or caminho == 'ir para traz' or caminho == 'para traz':
    print('Ok. Vamos voltar!')
elif caminho == 'esquerda' or caminho == 'ir para esquerda' or caminho == 'para esquerda':
    print('Ok. Vamos para a esquerda!')
elif caminho == 'direita' or caminho == 'ir para direita' or caminho == 'para direita':
    print('Ok. Vamos para a direita!')
elif caminho == 'parado' or caminho == 'ficar parado' or caminho == 'fica':
    print('Ok. Vamos ficar parados!')
else:
    print('Não entendi o seu comando')

#Tem que lembrar de repetir a variável sempre que o comando "or" for utilizado