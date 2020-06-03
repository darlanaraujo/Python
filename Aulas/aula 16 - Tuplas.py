'''
AULA 16 - VARIÁVEIS COMPOSTAS - TUPLAS

Variável composta são formadas por - TUPLAS () - LISTA [] - DICIONÁRIO {}

Ex. de Variável simples: lanche = hamburger
Toda vez que for feita uma nova atribuição para essa variável, o item dentro
dela será subistituido, ou seja, só pode ter 1 item por vez.
----------------------------------------------------------------------------
Ex. de Variável composta: lanche = (hambúrguer, suco, pizza, pudim)
Atenção! A TUPLA uma vez criada, ela não pode mudar o conteúdo dentro dela.

Para ter acesso ao conteúdo individual dentro da TUPLA, se usa os indices, que
vai de 0 até a quantidade de itens inseridos.

Ex. print(lanche[2]) = pizza
'''
# ======== FUNÇÃO DE LINHAS PARA O PROGRAMA ==============================
def linha():
    print('-'*40)
# ======== PRÁTICA E EXEMPLOS ============================================
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')

copia = lanche[:] #Essa função cria uma cópia da variável caso haja necessidade de mudar um conteudo e deixar a original

print('1)', lanche) #Mostra tudo dentro da tupla
linha()
print('2)', lanche[0]) #Mostra apenas o item no indice 0
linha()
print('3)', lanche[0:2]) #Mostra os itens de 0 a 1 (ele desconsidera o 2)
linha()
print('4)', lanche[1:]) #Mostra do indice 1 até o final
linha()
print('5)', lanche[:2]) #Mostra do inicio até o indice 1 (ja que o 2 é desconsiderado)
linha()
print('6)', lanche[-1]) #Mostra o último item dentro da tupla
linha()
print('7)', lanche[+2]) #Mostra o iten no indice 2 = pizza
linha()
# ======== FUNÇÃO PARA LER A QUANTIDADE DE ITENS DENTRO DA TUPLA =========

print('8)', len(lanche)) #Mostra a quantidade de itens nesse caso 4
linha()

# ======== USO DAS ESTRUTURAS DE REPETIÇÃO COM AS TUPLAS =================
'''
EX: for c in lanche:
Quando uso esse comando, é criado uma variável C e a cada loop o programa
vai colocar um item da TUPLA(lanche) dentro da variável C (uma por vez).
'''
#Nesse exemplo eu consigo mostrar a posição do item
for cont in range(0, len(lanche)):
    print(f'9) Eu vou comer {cont} {lanche[cont]}')
linha()
#Se não precisar de posição do item
for comida in lanche: #Para cada comida em lanche... mostre comida
    print(f'10) Eu vou comer {comida}') #Ele vai ler e mostrar os itens um por um.
linha()
#Se precisar da posição do item
for pos, comida in enumerate(lanche): #Para cada comida na posição em lanche... mostre comida e posição
    print(f'10) Eu vou comer {comida} na posição {pos}') #Ele vai ler e mostrar os itens um por um.
linha()

# ======== EXEMPLO DE FUNÇÃO PARA ORGANIZAR A TUPLA ======================
print(f'11) {sorted(lanche)}') #Essa função não muda a tupla, apenas mostra na tela organizado
linha()

# ======== ORDEM PARA UNIR VARIAS TUPLAS =================================
#Esse ex. mostra que ao juntar as tuplas ele não soma valores, apenas os une na ordem que estão
a = (2, 5, 4, 'a', 'b')
b = (5, 8, 1, 2, 'c', 'd')
c = a + b
print(c)

pessoa = ('Darlan', 35, 'M')
print(pessoa)

#Função para apagar variável
del(pessoa)
print(pessoa)

#Para saber se tem um item dentro da tupla e qual a sua quantidade
print(c.count(5))
print(c.count('a'))
print(c.count('j')) #Um item que não tenha na tupla vai mostrar 0

#Para saber a posição que um item se encontra na tupla
print(c.index(2)) #Quando há 2 itens de mesmo valor na tupla, ele vai mostrar o primeiro
print(c.index(5, 2)) #Para encontrar o proximo precisa colocar a partir do primeiro
print(c.index('d'))

''''# ======== EXEMPLO QUE NÃO DA CERTO PARA MOSTRAR VARIOS ITENS ============
salgado = ()
for c in range(0, 3):
    salgado = str(input('12) Nome do salgado: '))
print(f'{c} {salgado}') #No final ele vai mostrar apenas o último item digitado.
linha()

# Já o exemplo de baixo usando uma lista [] com a função append funciona.
salgado = []
for c in range(0, 3):
    salgado.append(str(input('13) Nome do salgado: ')))
for c in salgado:
    print(f'Eu vou comer {c}')
print('Comi pra caramba!')
print(f'13) {salgado}') #No final ele vai mostrar todos os itens digitado.
linha()'''