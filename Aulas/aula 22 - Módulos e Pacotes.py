'''
AULA 22 - Módulos e Pacotes

Modularização: É uma forma de dividir o seu programa para que a leitura e manutenção do código fique mais fácil.

As principais vantagens são, organização do código; Facilidade na manutenção; Ocultação de códigos detalhados;
reutilização em outros projetos.

Pacotes (biblíoteca): É a forma de organizar os modulos quando esses ficam grande, assim você pode separ os modulos
por assuntos e guarda-los em um lugar (pacotes) sem precisar criar vários modulos.

Um exemplo seria criar um pacote uteis e dentro dele separar as funcões por temas: números; strings; datas; cores; etc.
'''
# ============= PRÁTICA / TEORIA ======================================================================================

"""
Para criar um módulo o arquivo deve ter pelo menos uma funções. No modelo abaixo, temos 3 funções criadas, e posso
importa-las sitando a pasta e o modulo. from pasta import modulo.
"""
# Modelo importando um item dentro do modulo. Nesse caso a pasta modulos é só um local que o modulo uteis está dentro.
from modulos import uteiss
num = int(input('Digite um valor: '))
fat = uteiss.fatorial(num)
print(f'{fat}')
print(f'O dobro de {num} é {uteiss.dobro(num)}')
print(f'O triplo de {num} é {uteiss.triplo(num)}')

# Modelo importado de um pacote = modulos / modulo = numeros. Nesse caso a pasta modulos é um pacote e tudo que tem
# dentro dela faz parte do pacote.
from modulos import numeros

num = int(input('Digite outro valor: '))
print(numeros.fatorial(num))
print(numeros)

"""
Na criação do pacote, eu poderia faze-lo de duas maneiras.

Pacote com modulos: Eu poderia criar um pacorte chamado uteis, e dentro desse pacote eu colocaria vários modulos, cada
um com um nome e suas funções.

Pacote com pacotes: Nesse caso eu crio um pacote principal, e dentro dele crio várias pastas, cada um com um nome. E ao
invés de criar modulos, eu coloco as funções dentro do arquivo __init__.py. Assim cada pasta é um pacote e um modulo
ao mesmo tempo, e a importação se da pelo nome da pasta.

IMPORTANTE - Se um pacote principal que se chama uteis, tiver mais um (ou vários) chamado dados pacotes dentro dele,
e dentro desses outros pacortes tiver módulos. A forma de importação é FROM UTEIS IMPORT DADOS.

Mas caso dentro de um dos pacotes tenha outro pacote (ou vários) chamado nomes e dentro de cada um deles um módulo.
A forma de importação é FROM UTEIS.DADOS IMPORT NOMES
"""
