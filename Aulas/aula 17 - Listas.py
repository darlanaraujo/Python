'''
AULA 17 - VARIÁVEIS COMPOSTAS - LISTAS

Variável composta são formadas por - TUPLAS () - LISTA [] - DICIONÁRIO {}

Diferente das TUPLAS, as listas podem ser alteradas dentro do programa.

Ex:
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picole'
Nesse caso o 'pudim' seria substiruido pelo 'picole'.

No entando para acrescentar um novo item, não basta apenas dizer:
lanche = 'pastel'
Assim ele trocaria tudo dentro de lista pelo 'pastel'
'''

#Exemplo de um comando para mudar um item dentro de uma lista;
def titulo(txt):
    print()
    print(f'{txt:^50}')
    print('='*50)
# =====================================================================

titulo('TROCANDO UM ITENS NA LISTA')

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(f'{lanche} \033[33m<<<Lista original\033[m')

#Nesse caso o 'pudim' seria substiruido pelo 'picole'.
lanche[3] = 'picole'
print(f'{lanche} \033[33m<<<Lista alterada\033[m')
#No entando, eu não posso trocar um item em uma posição que não existe
#Ex. lanche[9] = 'coxinha' - porque o item 9 não existe.

#----------------------------------------------------------
titulo('ADICIONANDO ITENS NA LISTA')

#Para acrescentar um novo item, não basta apenas dizer:
lanche = ['pastel']
print(f'{lanche} \033[33m<<<Ele trocou toda a lista por apenas 1 item.\033[m')
#Assim ele trocaria tudo dentro de lista pelo apenas pelo 'pastel'

#A forma correta para acrescentar um novo item é usando o comando;

lanche.append('Coxinha')
lanche.append('Bolinho')
lanche.append('Kibe')
lanche.append('Pizza')
print(f'{lanche} \033[33m<<<Agora eu consigo adicionar novos itens\033[m')

#Outra forma para adicionar itens na lista em posições especificas;

lanche.insert(1,'Cachorro Quente')
print(f'{lanche} \033[33m<<<Aqui adicionei um intem entre os dois objetos\033[m')

#----------------------------------------------------------
titulo('REMOVENDO ITENS NA LISTA')
#Para apagar um elemento da lista, basta usar as funções;

del lanche[5]
print(f'{lanche} \033[33m<<<O item pizza foi apagado.\033[m')

#Outra forma; Esse comando se não tiver valor dentro das () apaga o último item da lista
lanche.pop(4)
print(f'{lanche} \033[33m<<<O item kibe foi apagado.\033[m')

#Outra forma para apagar pelo nome do item; O nome precisa está exatamente igual.
#Nessa opção, a melhor forma é usando a estrutura if;
if 'Bolinho' in lanche:
    lanche.remove('Bolinho')
    print(f'{lanche} \033[33m<<<O item bolinho foi apagado\033[m')
else:
    print(f'{lanche} \033[33m<<<O item bolinho não foi apagado\033[m')

#----------------------------------------------------------------------
titulo('CRIANDO LISTAS COM A FUNÇÃO RANGE')

#Nessa opção criamos uma lista de números com a função range;
valores = list(range(2, 11))
print(f'{valores} \033[33m<<<Ele criou uma lista de 2 a 10 organizada\033[m')

#Outra opção é fazer a função range com 3 elementos;
valores = list(range(0, 11, 2))
print(f'{valores} \033[33m<<<Ele cria uma lista de 0 a 10 pulando 2 casas\033[m')

#-----------------------------------------------------------------------
titulo('ORGANIZANDO UMA LISTA COM A FUNÇÃO SORT()')

valores = [8, 2, 5, 4, 9, 3, 0]
print(f'{valores} \033[33m<<<Os itens estão desorganizados na lista\033[m')

#Para organizar, basta usar a função sort();
valores.sort()
print(f'{valores} \033[33m<<<Os números ficam organizados\033[m')

#Para organizar na ordem inversa;
valores.sort(reverse=True)
print(f'{valores} \033[33m<<<Os números ficam invertidos\033[m')

#-----------------------------------------------------------------------
titulo('FUNÇÃO LEN PARA LER A LISTA')

print(f'Essa lista tem {len(valores)} elementos \033[33m<<<Assim consigo saber quantos itens tem na lista\033[m')

#----------------------------------------------------------------------
titulo('AULA PRATICA')

'''valores = list() #Ou poderia ser valores = []

for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}º número: ')))
print(f'{valores} \033[33m<<<Os números digitados foram inseridos na lista\033[m')

for pos, valor in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {valor}')
print('Fim da listagem')'''

#---------------------------------------------------------------------
titulo('CLONAGEM DA LISTAS')

a = [2, 3, 4, 7] #Lista original
b = a #Cópia da lista
b[2] = 8 #Nesse comando, ao trocar um item dentro de uma cópia, muda tbm a lista original.

#Quando vc iguá-la uma lista, é criada uma ligação entre elas, e as duas mudam de acordo uma com a outra.
print(f'Lista A {a} \033[33m<<<Lista original\033[m')
print(f'Lista B {b} \033[33m<<<Clonagem da lista\033[m')

titulo('CÓPIA REAL DE UMA LISTA')
#A forma correta para se criar uma cópia independente é essa;

a = [1, 2, 3, 4, 5]
b = a[:] #ao colocar [:] ao final da variável eu crio uma cópia real
b[2] = 9

#Agora ao trocar um item dentro da cópia, a lista original não muda.
print(f'Lista A {a} \033[33m<<<Lista original\033[m')
print(f'Lista B {b} \033[33m<<<Cópia da lista\033[m')