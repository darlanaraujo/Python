'''
AULA 18 - VARIÁVEIS COMPOSTAS - LISTAS

Variável composta são formadas por - TUPLAS () - LISTA [] - DICIONÁRIO {}

Formas de declaração de uma lista: dados = [] ou dados = list()

Diferente das TUPLAS, as listas podem ser alteradas dentro do programa.
'''

# ================= EXEMPLOS ==============================================
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)
print(dados[0])
print(dados[1])
'''No exemplo acima, criamos uma variável composta com 2 dados. Para ter
acesso ao conteudo, podemos mostrar toda a lista, ou seu conteudo individual'''

# ---------------------------------------------------------------------------
'''Agora vamos ver exemplos de como colocar listas dentro de outras listas'''
pessoas = list()
pessoas.append(dados[:]) #lembrando que ao usar o [:] faço uma cópia da lista original.
#Eu tenho duas formas de usar o append. Posso colocar apenas 1 dado, ou vários.
pessoas.append('Darlan')
pessoas.append(35) #Nesse caso só consigo colocar 1 dado por vez.
pessoas.append(['Maria', 19, 'João', 32]) #Usando [] posso colocar vários.
print(pessoas)
print(len(pessoas))
print(pessoas[0]) #Mostra Pedro, 25 (a cópia de dados)
print(pessoas[1]) #Mostra apenas Darlan
print(pessoas[2]) #Mostra apenas 35
print(pessoas[3]) #Mostra Maria, 19, João, 32
'''No entando, ao adicionar vários itens, todos eles assumem um indice, assim
como ao adicionar 1 por vez, cada um assume um indice individual'''
# ----------------------------------------------------------------------------
'''A forma correta para colocar os indices separados de forma organizada é
usar [] para cada elemento com seu respectivo par.'''

galera = [['Darlan', 35], ['Carol', 27], ['Davi', 0]]
#porem no append isso não é possível. Ou coloca tudo junto dentro do mesmo []
#Ou separa um por vez.
#pessoas2.append(['Darlan', 35], ['Carol', 27], ['Davi', 0]) #Forma errada!
#pessoas2.append(['Darlan', 35, 'Carol', 27, 'Davi', 0) #Forma correta!

'''Fateamento de uma lista dentro de outra lista'''
print(galera[0][0])
#O primeiro [] mostra a lista completa. No caso: Darlan, 35
#O segundo [] mostra 1 item dentro dessa lista. No caso: Darlan

'''Se eu quiser fatear ainda mais posso usar 3 [], assim busco letra por letra'''
print(galera[0][0][0])
##O primeiro [] mostra a lista completa. No caso: Darlan, 35
#O segundo [] mostra 1 item dentro dessa lista. No caso: Darlan
#O terceiro [] mostra a primeira letra. No caso: D

# ============== FORMA DE SE USAR REPETIÇÕES COM AS LITAS =====================
print('='*30)
#Nesse exemplo mostramos todas as informações na lista
for p in galera:
    print(p)

print('='*30)
#Nesse exemplo posso mostrar apenas uma informação em cada lista
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

print('='*30)
#Nesse exemplo vou pegar os dados digitados pelo usuário;
turma = list()
lista = list()
for c in range(0, 3):
    lista.append(str(input('Digite um nome: ')))
    lista.append(int(input('Digite a idade: ')))
    lista.append(str(input('Digite o sexo: ')))
    #Depois de coletar os dados digitados e guarda-los na lista.
    turma.append(lista[:]) #Jogo todos os dados para turma em forma de cópia.
    lista.clear() #Por fim limpo a lista para coletar dados novamente

print(turma)
for pos, pesoas in enumerate(turma):
    print(f'{turma[pos][0]} do sexo {turma[pos][2]} tem {turma[pos][1]} anos de idade.')
