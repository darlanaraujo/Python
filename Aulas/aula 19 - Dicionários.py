'''
AULA 19 - VARIÁVEIS COMPOSTAS - DICIONÁRIOS

Variável composta são formadas por - TUPLAS () - LISTA [] - DICIONÁRIO {}

A principal caracteristica do Dicionário em relação as outras  variáveis compostas é a possibilidade de dar nomes aos
indices. No dicionário não preciso fazer uma varredura pelos números, posso simplesmente dar um nome para o valor.

Posso delcarar uma variável como dicionário de duas formas: dados = {} ou dados = dict()

Um dicionário é dividido em 3 elementos: itens, chaves ou valores
Ex: alunos = {'nome': 'darlan', 'idade': 35}
print(alunos.values()) - Os valores são: darlan, 35
print(alunos.keys()) - As chaves são: nome, idade
print(alunos.items()) - Os itens são: 'nome': 'darlan', 'idade': 35

Obrigatoriamente, ao declarar um dicionário, você tem que definir as chaves para validar os valores.
Ex: nome = {'Darlan', 35, 'M'} - Você teria os valores, mas sem as chaves, o programa até aceita, mas você não consegue
exibir os resultados de forma separada.
'''

def linhas(txt):
    print(f'{txt:-^80}')

# ======================== EXEMPLOS ===================================================================================
linhas(' EXEMPLO ')

dados = {'nome':'Pedro', 'idade':25}
#Para mostrar esse resultado:

print(dados['nome']) # == Pedro
print(dados['idade']) # == 25

# print formatado!
print(f'O {dados["nome"]} tem {dados["idade"]} anos.')
print()
# ======================== ADICIONANDO NOVOS DADOS NA VARIÁVEL ========================================================
linhas(' ADICIONANDO NOVOS DADOS ')
#Para adicionar mais um elemento ao dícionário a função .append() não funciona.
# Para adicionar basta digitar:

dados['sexo']='M' #Com isso a estrutura ficaria:
print(dados['sexo'])
print(dados) # == dados = {'nome':'Pedro', 'idade':25, 'sexo':'M'}
print()
# ======================== REMOVENDO DADOS DA VARIÁVEL ================================================================
linhas(' REMOVENDO DADOS ')
#Para remover um elemento basta usar a função DEL.
del dados['idade'] #Assim o valor e o elemento são eliminados.
print(dados)
print()
# ======================== OUTRA FORMA DE ORGANIZAR UM DICIONÁRIO =====================================================
linhas(' OUTRA FORMA DE ORGANIZAR ')
filmes = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
print(filmes)
print(filmes['titulo'])
print(filmes['ano'])
print(filmes['diretor'])
print()
# ======================= OS 3 ELEMENTOS DE UM DICIONÁRIO =============================================================
linhas(' OS 3 ELEMENTOS DE UM DICIONÁRIO ')
# Itens, Chaves ou Valores

print(filmes.values()) # Os valores são: Star Wars, 1977, George Lucas
print(filmes.keys()) # As chaves são: titulo, ano, diretor
print(filmes.items()) # os itens são: todos os conteúdos
print()
# ======================= USANDO FOR COM DICINOÁRIO ===================================================================
linhas(' USANDO FOR COM DICIONÁRIO ')

# No caso do dicionário, o FOR não se usa enumerate().

for k, v in filmes.items(): #K de keys() - V de Values()
    print(f'O {k} é {v}')
print('-'*30)

for k in filmes.keys():
    print(k)
print('-'*30)

for v in filmes.values():
    print(v)
print('-'*30)

print()
# ======================= JUNTANDO LISTAS COM DICIONÁRIOS =============================================================
linhas(' JUNTANDO LISTAS COM DICIONÁRIOS ')

# ATENÇÃO! A ordem é um dicionário dentro da lista!
locadora = []
locadora.append(filmes)
print(locadora)

# NOTA IMPORTANTE: Não posso ter dois dicionários com o mesmo nome. Ou eu coloco os novos dados dentro do dicionário
# existente, ou se eu fizer como no exemplos abaixo, eu estou subistituindo um pelo outro.

# Uma maneira de burla isso, é antes de fazer o dicionário com o mesmo nome, eu adicioná-lo em uma lista. Como no
# exemplo a cima!

filmes = {'titulo': 'Avangers', 'ano': 2012, 'diretor': 'Joss Whedon'}
locadora.append(filmes)
print(locadora)
print(filmes)

filmes = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
locadora.append(filmes)
print(locadora)
print(filmes)
print()
# ========================== SEPARANDO OS ITENS DENTRO DA LISTA =======================================================
linhas(' SEPARANDO OS ITENS DA LISTA ')
# Agora para mostrar os resultados, uso o formato abaixo.

print(locadora[0]['titulo'])
print(locadora[0]['ano'])
print(locadora[0]['diretor'])
print()
# ========================= LENDO DADOS PARA UM DICIONÁRIO/LISTA ======================================================
linhas(' LENDO DADOS PARA UM DICIONÁRIO/LISTA ')

# ATENÇÃO ISSO É MUITO IMPORTANTE: Não é possivel fazer uma cópia de um dicionário para uma lista usando fateamento [:].
# Existe um metodo interno .copy()

estado = {}
brasil = []

for c in range(0, 3):
    # O objetivo aqui é colocar o estado e a sigla dentro do dicionário 3x. Porém um dado novo vai substiruir o velho!
    # Por isso a necessidade de após coletado, ser inserido em uma lista. Dentro da lista teremos 3 dicionários!
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    # Agora vamos colocar esses dados 1 por vez dentro da lista. Porém, não é possível fazer uma cópia usando fateamento
    # Nesse caso vamos usar o metodo .copy()
    brasil.append(estado.copy())

# Uma forma de mostrar os dados mais organizados, é usando um laço dentro de outro. Sendo o primeiro para a lista e o
# segundo para os dicionários;

for estados in brasil:
    for keys, valores in estados.items():
        print(f'O campo: {keys} tem valor: {valores}')
print('-'*60)
for estados in brasil:
    for keys, valores in estados.items():
        print(f'{keys}: {valores}')

