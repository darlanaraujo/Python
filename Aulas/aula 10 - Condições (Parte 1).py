'''
CURSO DE PYTHON - ESTUDO DE CONDIÇÕES - PARTE 1
'''

'''
#Exemplo de uma extrutura condicional aninhado:

if carro.esquerda():
    blocoTrue
else:
    blocoFalse
    
'''
#Existe dois tipos de condição; Condição simples, ela só tem a condicional if.
#A condição composta tem a condição if e else.

'''print('{:=^40}'.format('EXEMPLO CONDIÇÃO ANINHADA'))
print()
tempo=int(input('Quantos anos tem seu carro? '))
if tempo <=1:
    print('Um carro com {} ano é considerado um carro zero'.format(tempo))
else:
    if tempo <=3:
        print('Um carro com {} anos é considerado um carro novo'.format(tempo))
    else:
        if tempo <=6:
            print('Um carro com {} anos é considerado um carro com meia vida'.format(tempo))
        else:
            print('Um carro com {} anos é considerado um carro velho'.format(tempo))
print()
print('{:=^40}'.format('FIM DO PROGRAMA'))'''

#Abaixo segue uma opção mais curta que daria o mesmo resultado

'''
print('{:=^60}'.format('EXEMPLO CONDIÇÃO ANINHADA SIMPLIFICADA'))
print()
tempo=int(input('Quantos anos tem seu carro? '))
print('Um carro com {} anos é considerado um carro novo'.format(tempo) if tempo<=3 else 'Um carro com {} anos é considerado um carro velho'.format(tempo))
print()
print('{:=^60}'.format('FIM DO PROGRAMA'))
'''
#Exemplos de comandos

'''print('{:=^40}'.format('INÍCIO DO PROGRAMA'))
nome=str(input('Olá, Qaual o seu nome? ')).strip().title()
if 'Araujo' in nome:
    print('Nossa! Nós temos o mesmo sobrenome.')
print('Seja bem-vindo(a) {}, prazer termos você em nosso programa'.format(nome))
print('{:=^40}'.format('FIM DO PROGRAMA'))'''


print('{:=^40}'.format('INÍCIO DO PROGRAMA'))
print()
print('Instruções do programa! Utilize . para definir sua nota. Ex 5.5')
n1=float(input('Qual a sua primeira nota? '))
n2=float(input('Qual a sua segunda nota? '))
m=(n1 + n2)/2
print('A sua primeira nota foi: {:.1f}'.format(n1))
print('A sua segunda nota foi: {:.1f}'.format(n2))
print('A sua média nesse semestre ficou: {:.2f}'.format(m))
if m <=2.9:
    print('Além de não passar, sua média ficou muito baixa!')
else:
    if m <=5.9:
        print('Que pena! Sua média não foi suficiente para passar.')
    else:
        if m == 6.0:
            print('Ufá! foi por pouco. Você ficou no limite da médida')
        else:
            if m <=9.0:
                print('Meus parabéns, você passou nesse semestre!')
            else:
                print('Que isso! Você tirou a média máxima esse semestre. PARABÉNS!')
print()
print('{:=^40}'.format('FIM DO PROGRAMA'))




