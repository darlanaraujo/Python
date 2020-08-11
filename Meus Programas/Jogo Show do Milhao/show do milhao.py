

# ===================== IMPORTAÇÕES ===================================================================================
from time import sleep
from random import randint
import pygame

# ===================== VARIAVEIS GLOBAIS =============================================================================
# Nome do arquivo para salvar dados do jogo;
arq = 'jogoshowmilhao.txt'
nome = 'Nome Jogador'

# Tabela de cores;
sc = '\033[m'       # 0 = Sem cor
br = '\033[30m'     # 1 = Branco
vm = '\033[31m'     # 2 = Vermelho
vd = '\033[32m'     # 3 = Verde
am = '\033[33m'     # 4 = Amarelo
az = '\033[34m'     # 5 = Azul
rx = '\033[35m'     # 6 = Roxo
# Cores com fundo;
fvm = '\033[41;30m' # 7 = Fundo Vermelho Letra Branca

# Ajudas do jogo;
pulo = 3
carta = 1
convidado = 1
colega = 1

# Definição da posição do jogador na partida;
p = 0

# Definição dos valores para cada rodada;
valor = ['R$ 1.000,00', 'R$ 2.000,00', 'R$ 3.000,00', 'R$ 4.000,00', 'R$ 5.000,00',
         'R$ 10.000,00', 'R$ 20.000,00', 'R$ 30.000,00', 'R$ 40.000,00', 'R$ 50.000,00',
         'R$ 100.000,00', 'R$ 200.000,00', 'R$ 300.000,00', 'R$ 400.000,00', 'R$ 500.000,00', 'R$ 1.000.000,00']

# Definição para a variável de premio que será exibida ao termino da jogada e mostrá-ra o valor ganho pelo jogador.
premio = 'R$ 0,00'
acerto = 'R$ 0,00'
errar = 'R$ 0,00'
parar = 'R$ 0,00'
# ===================== PERGUNTAS DO JOGO =============================================================================
# Formulário base para as perguntas;
# Pergunta 0
f'{fvm}>>>  msg   {sc}'
f'\n{am}A) {br}msg'
f'\n{am}B) {br}msg'
f'\n{am}C) {br}msg'
f'\n{am}D) {br}msg'

nivel1 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Em que estado brasileiro nasceu a apresentadora Xuxa?   {sc}'
    f'\n{am}A) {br}RIO DE JANEIRO'
    f'\n{am}B) {br}RIO GRANDE DO SUL'
    f'\n{am}C) {br}SANTA CATARINA'
    f'\n{am}D) {br}GOIÁS',
    # Pergunta 1
    f'{fvm}>>>  Qual é o nome dado ao estado da água em forma de gelo?   {sc}'
    f'\n{am}A) {br}LÍQUIDO'
    f'\n{am}B) {br}SÓLIDO'
    f'\n{am}C) {br}GASOSO'
    f'\n{am}D) {br}VAPOROSO',
    # Pergunta 2
    f'{fvm}>>>  Qual era o apelido da cantora Elis Regina?   {sc}'
    f'\n{am}A) {br}GAUCHINHA'
    f'\n{am}B) {br}PAULISTINHA'
    f'\n{am}C) {br}PIMENTINHA'
    f'\n{am}D) {br}ANDORINHA',
    # Pergunta 3
    f'{fvm}>>>  Quem é a namorada do Mickey?   {sc}'
    f'\n{am}A) {br}MARGARIDA'
    f'\n{am}B) {br}MINNIE'
    f'\n{am}C) {br}A PEQUENA SEREIA'
    f'\n{am}D) {br}OLÍVIA PALITO',
    # Pergunta 4
    f'{fvm}>>>  Fidel Castro nasceu em que país?   {sc}'
    f'\n{am}A) {br}JAMAICA'
    f'\n{am}B) {br}CUBA'
    f'\n{am}C) {br}EL SALVADOR'
    f'\n{am}D) {br}MÉXICO',
    # Pergunta 5
    f'{fvm}>>>  Quem proclamou a república no Brasil em 1889?   {sc}'
    f'\n{am}A) {br}DUQUE DE CAXIAS'
    f'\n{am}B) {br}MARECHAL RONDON'
    f'\n{am}C) {br}DOM PEDRO II'
    f'\n{am}D) {br}MARECHAL DEODORO',
    # Pergunta 6
    f'{fvm}>>>  Quem é o patrono do exército brasileiro?   {sc}'
    f'\n{am}A) {br}MARECHAL DEODORO'
    f'\n{am}B) {br}BARÃO DE MAUÁ'
    f'\n{am}C) {br}DUQUE DE CAXIAS'
    f'\n{am}D) {br}MARQUÊS DE POMBAL',
    # Pergunta 7
    f'{fvm}>>>  Qual é o signo do zodíaco de quem nasce no dia do ano-novo?   {sc}'
    f'\n{am}A) {br}VIRGEM'
    f'\n{am}B) {br}AQUÁRIO'
    f'\n{am}C) {br}CAPRICÓRNIO'
    f'\n{am}D) {br}ÁRIES',
    # Pergunta 8
    f'{fvm}>>>  A água ferve a quantos graus centígrados?   {sc}'
    f'\n{am}A) {br}200'
    f'\n{am}B) {br}100'
    f'\n{am}C) {br}170'
    f'\n{am}D) {br}220',
    # Pergunta 9
    f'{fvm}>>>  Quando é comemorado o dia da independência do Brasil?   {sc}'
    f'\n{am}A) {br}21 DE ABRIL'
    f'\n{am}B) {br}12 DE OUTUBRO'
    f'\n{am}C) {br}7 DE SETEMBRO'
    f'\n{am}D) {br}25 DE DEZEMBRO',
    # Pergunta 10
    f'{fvm}>>>  Segundo a crença popular, a mula-sem-cabeça é mulher de quem?   {sc}'
    f'\n{am}A) {br}DO COROINHA'
    f'\n{am}B) {br}DO PADRE'
    f'\n{am}C) {br}DO SACRISTÃO'
    f'\n{am}D) {br}DO BISPO',
    # Pergunta 11
    f'{fvm}>>>  Como é chamada a doença que causa perda desigual da melanina?   {sc}'
    f'\n{am}A) {br}ASTIGMATISMO'
    f'\n{am}B) {br}TENDINITE'
    f'\n{am}C) {br}VITILIGO'
    f'\n{am}D) {br}VITINGA',
    # Pergunta 12
    f'{fvm}>>>  Quem realizou a primeira cirurgia de ponte de safena no Brasil?   {sc}'
    f'\n{am}A) {br}DR. ZERBINI'
    f'\n{am}B) {br}DR. FRITZ'
    f'\n{am}C) {br}DR. JATENE'
    f'\n{am}D) {br}DR. GALLIGARI',
    # Pergunta 13
    f'{fvm}>>>  Qual é a moeda oficial da Alemanha?   {sc}'
    f'\n{am}A) {br}LIRA'
    f'\n{am}B) {br}MARCO'
    f'\n{am}C) {br}FRANCO'
    f'\n{am}D) {br}LIBRA',
    # Pergunta 14
    f'{fvm}>>>  Quem foi o assassino de Lee Harvey Oswald?   {sc}'
    f'\n{am}A) {br}JACK RUBY'
    f'\n{am}B) {br}JOHN WILKES BOOTH'
    f'\n{am}C) {br}PAT GARRET'
    f'\n{am}D) {br}CHARLOTTE CORDAY',
    # Pergunta 15
    f'{fvm}>>>  Nas histórias do Snoopy, qual é o nome do passarinho?   {sc}'
    f'\n{am}A) {br}PIU-PIU'
    f'\n{am}B) {br}WOODSTOCK'
    f'\n{am}C) {br}CANARINHO'
    f'\n{am}D) {br}ROUXINOL',
    # Pergunta 16
    f'{fvm}>>>  Que metal avermelhado cria uma camada esverdeada em contato com a umidade?   {sc}'
    f'\n{am}A) {br}FERRO'
    f'\n{am}B) {br}COBRE'
    f'\n{am}C) {br}MERCÚRIO'
    f'\n{am}D) {br}AÇO',
    # Pergunta 17
    f'{fvm}>>>  Que humorista, falecido em 1999, foi baterista de Raul Seixas?   {sc}'
    f'\n{am}A) {br}LILICO'
    f'\n{am}B) {br}RONI CÓCEGAS'
    f'\n{am}C) {br}GRANDE OTELO'
    f'\n{am}D) {br}MAZZAROPI',
    # Pergunta 18
    f'{fvm}>>>  O que os filatelistas colecionam?   {sc}'
    f'\n{am}A) {br}QUADROS'
    f'\n{am}B) {br}MOEDAS'
    f'\n{am}C) {br}SELOS'
    f'\n{am}D) {br}FIGURINHAS',
    # Pergunta 19
    f'{fvm}>>>  Quando começou e terminou a Primeira Guerra Mundial?   {sc}'
    f'\n{am}A) {br}1914 - 1919'
    f'\n{am}B) {br}1039 - 1945'
    f'\n{am}C) {br}1921 - 1932'
    f'\n{am}D) {br}1912 - 1915',
],
    'resposta':['B', 'B', 'C', 'B', 'B', 'D', 'C', 'C', 'B', 'C', 'B', 'C', 'C', 'B', 'A', 'B', 'B', 'B', 'C', 'A']
}

nivel2 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Quantos jogadores um jogo de vôlei reúne na quadra?   {sc}'
    f'\n{am}A) {br}SEIS'
    f'\n{am}B) {br}OITO'
    f'\n{am}C) {br}DEZ'
    f'\n{am}D) {br}DOZE',
    # Pergunta 1
    f'{fvm}>>>  Que imperador pôs fogo em Roma?   {sc}'
    f'\n{am}A) {br}TRAJANO'
    f'\n{am}B) {br}NERO'
    f'\n{am}C) {br}BRUTOS'
    f'\n{am}D) {br}CALÍGULA',
    # Pergunta 2
    f'{fvm}>>>  Como é chamado quem nasce em Milão, na Itália?   {sc}'
    f'\n{am}A) {br}MILANENSE'
    f'\n{am}B) {br}MILANOSO'
    f'\n{am}C) {br}MILISTA'
    f'\n{am}D) {br}MILANÊS',
    # Pergunta 3
    f'{fvm}>>>  O que é um oboé?   {sc}'
    f'\n{am}A) {br}VULCÃO'
    f'\n{am}B) {br}COMIDA'
    f'\n{am}C) {br}INSTRUMENTO MUSICAL'
    f'\n{am}D) {br}TRIBO INDÍGENA',
    # Pergunta 4
    f'{fvm}>>>  O que é gôndola?   {sc}'
    f'\n{am}A) {br}EMBARCAÇÃO'
    f'\n{am}B) {br}BRINQUEDO'
    f'\n{am}C) {br}MÚSICA'
    f'\n{am}D) {br}SÍMBOLO',
    # Pergunta 5
    f'{fvm}>>>  Como é chamada a cantora que representa o papel principal em uma ópera?   {sc}'
    f'\n{am}A) {br}PRIMEIRA DAMA'
    f'\n{am}B) {br}DONA-PRIMA'
    f'\n{am}C) {br}PRIMA-DONA'
    f'\n{am}D) {br}OBRA-PRIMA',
    # Pergunta 6
    f'{fvm}>>>  Que rio corta a cidade de Londres, na Inglaterra?   {sc}'
    f'\n{am}A) {br}TÂMISA'
    f'\n{am}B) {br}SENA'
    f'\n{am}C) {br}RENO'
    f'\n{am}D) {br}AUBE',
    # Pergunta 7
    f'{fvm}>>>  Qual cantor ficou conhecido como “O rei da voz”?   {sc}'
    f'\n{am}A) {br}ORLANDO SILVA'
    f'\n{am}B) {br}VICENTE CELESTINO'
    f'\n{am}C) {br}FRANCISCO ALVES'
    f'\n{am}D) {br}CARLOS GALHARDO',
    # Pergunta 8
    f'{fvm}>>>  Quantos quilates tem o ouro puro?   {sc}'
    f'\n{am}A) {br}18'
    f'\n{am}B) {br}20'
    f'\n{am}C) {br}24'
    f'\n{am}D) {br}30',
    # Pergunta 9
    f'{fvm}>>>  De quantos em quantos anos aparece o cometa Halley?   {sc}'
    f'\n{am}A) {br}57 ANOS'
    f'\n{am}B) {br}67 ANOS'
    f'\n{am}C) {br}76 ANOS'
    f'\n{am}D) {br}79 ANOS',
    # Pergunta 10
    f'{fvm}>>>  O que são meninges?   {sc}'
    f'\n{am}A) {br}CÉLULAS'
    f'\n{am}B) {br}NERVOS'
    f'\n{am}C) {br}MEMBRANAS'
    f'\n{am}D) {br}MÚSCULOS',
    # Pergunta 11
    f'{fvm}>>>  Como é chamada a bola de gelo e poeira que orbita em torno do sol?   {sc}'
    f'\n{am}A) {br}COMETA'
    f'\n{am}B) {br}METEORITO'
    f'\n{am}C) {br}CAMADA DE OZÔNIO'
    f'\n{am}D) {br}ESTRELA DALVA',
    # Pergunta 12
    f'{fvm}>>>  Qual a ciência que estuda a distribuição dos animais?   {sc}'
    f'\n{am}A) {br}ZOOTERAPIA'
    f'\n{am}B) {br}ZOOGEOGRAFIA'
    f'\n{am}C) {br}ZODÍACO'
    f'\n{am}D) {br}ZOOMETRIA',
    # Pergunta 13
    f'{fvm}>>>  A Bélgica é:   {sc}'
    f'\n{am}A) {br}UMA REPÚBLICA'
    f'\n{am}B) {br}UMA MONARQUIA CONSTITUCIONAL'
    f'\n{am}C) {br}UM EMIRADO'
    f'\n{am}D) {br}UM PRINCIPADO',
    # Pergunta 14
    f'{fvm}>>>  Que parte do corpo humano é infectada pela cólera?   {sc}'
    f'\n{am}A) {br}GARGANTA'
    f'\n{am}B) {br}INTESTINO'
    f'\n{am}C) {br}PULMÔES'
    f'\n{am}D) {br}RINS',
    # Pergunta 15
    f'{fvm}>>>  A união do espermatozóide com o óvulo origina uma célula chamada:   {sc}'
    f'\n{am}A) {br}ZIGOTO'
    f'\n{am}B) {br}BIGOTO'
    f'\n{am}C) {br}FETO'
    f'\n{am}D) {br}GAROTO',
    # Pergunta 16
    f'{fvm}>>>  A que país pertence a ilha de Terra Nova?   {sc}'
    f'\n{am}A) {br}ESTADOS UNIDOS'
    f'\n{am}B) {br}DINAMARCA'
    f'\n{am}C) {br}CANADÁ'
    f'\n{am}D) {br}FRANÇA',
    # Pergunta 17
    f'{fvm}>>>  De quem é este verso: “A praça é do povo, como o céu é do condor”?   {sc}'
    f'\n{am}A) {br}TOBIAS BARRETO'
    f'\n{am}B) {br}DORIVAL CAIMI'
    f'\n{am}C) {br}MACHADO DE ASSIS'
    f'\n{am}D) {br}CASTRO ALVES',
    # Pergunta 18
    f'{fvm}>>>  Que nome recebe a foz de um rio que se abre para o mar?   {sc}'
    f'\n{am}A) {br}ALAGADO'
    f'\n{am}B) {br}MANGUEZAL'
    f'\n{am}C) {br}PÂNTANO'
    f'\n{am}D) {br}ESTUÁRIO',
    # Pergunta 19
    f'{fvm}>>>  Em que ano Ayrton Senna venceu o primeiro campeonato de Fórmula 1?   {sc}'
    f'\n{am}A) {br}1987'
    f'\n{am}B) {br}1990'
    f'\n{am}C) {br}1985'
    f'\n{am}D) {br}1988',
],
    'resposta':['D', 'B', 'D', 'C', 'A', 'C', 'A', 'C', 'C', 'C', 'C', 'A', 'B', 'B', 'B', 'A', 'C', 'D', 'D', 'D',]
}

nivel3 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Quem disse a frase: “Vim, vi e venci”?   {sc}'
    f'\n{am}A) {br}JÚLIO CÉSAR'
    f'\n{am}B) {br}CALÍGULA'
    f'\n{am}C) {br}NERO'
    f'\n{am}D) {br}MARCO ANTÔNIO',
    # Pergunta 1
    f'{fvm}>>>  Beirute é a capital de que país?   {sc}'
    f'\n{am}A) {br}SÍRIA'
    f'\n{am}B) {br}NEPAL'
    f'\n{am}C) {br}MONGÓLIA'
    f'\n{am}D) {br}LÍBANO',
    # Pergunta 2
    f'{fvm}>>>  O que é um contratorpedeiro?   {sc}'
    f'\n{am}A) {br}TANQUE'
    f'\n{am}B) {br}NAVIO DE GUERRA'
    f'\n{am}C) {br}DIRIGÍVEL'
    f'\n{am}D) {br}AVIÃO DE CAÇA',
    # Pergunta 3
    f'{fvm}>>>  Em 1991, que esportista americano se afastou do basquete por ser HIV positivo?   {sc}'
    f'\n{am}A) {br}MICHAEL JORDAN'
    f'\n{am}B) {br}MAGIC JOHNSON'
    f'\n{am}C) {br}DENNIS RODMAN'
    f'\n{am}D) {br}MIKE TYSON',
    # Pergunta 4
    f'{fvm}>>>  A que categoria pertence o cavalo-marinho?   {sc}'
    f'\n{am}A) {br}MOLUSCO'
    f'\n{am}B) {br}CRUSTÁCEO'
    f'\n{am}C) {br}PEIXE'
    f'\n{am}D) {br}MAMÍFERO',
    # Pergunta 5
    f'{fvm}>>>  Em que cidade foram realizados os jogos olímpicos de 2000?   {sc}'
    f'\n{am}A) {br}MUNIQUE'
    f'\n{am}B) {br}SIDNEY'
    f'\n{am}C) {br}TÓQUIO'
    f'\n{am}D) {br}ATLANTA',
    # Pergunta 6
    f'{fvm}>>>  Qual desses astros de filmes de ação é belga?   {sc}'
    f'\n{am}A) {br}ARNOLD SCHWARZENEGGER'
    f'\n{am}B) {br}SYLVESTER STALLONE'
    f'\n{am}C) {br}STEVEN SEAGAL'
    f'\n{am}D) {br}JEAN CLAUDE VAN DAMME',
    # Pergunta 7
    f'{fvm}>>>  Qual presidente brasileiro instituiu o AI-5?   {sc}'
    f'\n{am}A) {br}COSTA E SILVA'
    f'\n{am}B) {br}ERNESTO GEISEL'
    f'\n{am}C) {br}JOÃO FIGUEIREDO'
    f'\n{am}D) {br}ITAMAR FRANCO',
    # Pergunta 8
    f'{fvm}>>>  O que significa literalmente Perestroika?   {sc}'
    f'\n{am}A) {br}CONVERSÃO'
    f'\n{am}B) {br}INVOLUÇÃO'
    f'\n{am}C) {br}REESTRUTURAÇÃO'
    f'\n{am}D) {br}REGRESSÃO',
    # Pergunta 9
    f'{fvm}>>>  Qual desses quatro pesos é o mais leve?  {sc}'
    f'\n{am}A) {br}10 ONÇAS'
    f'\n{am}B) {br}10 GRAMAS'
    f'\n{am}C) {br}10 QUILOS'
    f'\n{am}D) {br}10 LIBRAS',
    # Pergunta 10
    f'{fvm}>>>  Qual a origem da palavra folclore?   {sc}'
    f'\n{am}A) {br}HOLANDESA'
    f'\n{am}B) {br}INGLESA'
    f'\n{am}C) {br}FRANCESA'
    f'\n{am}D) {br}BRASILEIRA',
    # Pergunta 11
    f'{fvm}>>>  Quem ganhou a 1a medalha de ouro olímpico para o Brasil?   {sc}'
    f'\n{am}A) {br}AFRANIO ANTONIO COSTA'
    f'\n{am}B) {br}GUILHERME PARAENSE'
    f'\n{am}C) {br}FERNANDO SOLEDADE'
    f'\n{am}D) {br}SEBASTIÃO WOLF',
    # Pergunta 12
    f'{fvm}>>>  Que pintor francês consagrou a mulher taitiana em suas telas?   {sc}'
    f'\n{am}A) {br}RENOIR'
    f'\n{am}B) {br}GAUGUIN'
    f'\n{am}C) {br}CÉZANNE'
    f'\n{am}D) {br}MONET',
    # Pergunta 13
    f'{fvm}>>>  Qual foi a primeira mulher a entrar no “hall da fama” do rock and roll?   {sc}'
    f'\n{am}A) {br}JANIS JOPLIN'
    f'\n{am}B) {br}CAROLE KING'
    f'\n{am}C) {br}ARETHA FRANKLIN'
    f'\n{am}D) {br}DIANA ROSS',
    # Pergunta 14
    f'{fvm}>>>  Nova Caledônia faz parte da:   {sc}'
    f'\n{am}A) {br}MICRONÉSIA'
    f'\n{am}B) {br}MELANÉSIA'
    f'\n{am}C) {br}POLINÉSIA'
    f'\n{am}D) {br}INDONÉSIA',
    # Pergunta 15
    f'{fvm}>>>  Qual destas seleções nunca jogou uma final de copa?   {sc}'
    f'\n{am}A) {br}ESPANHA'
    f'\n{am}B) {br}SUÉCIA'
    f'\n{am}C) {br}HUNGRIA'
    f'\n{am}D) {br}FRANÇA',
    # Pergunta 16
    f'{fvm}>>>  Qual é o país que tem uma árvore estampada na bandeira?   {sc}'
    f'\n{am}A) {br}EGITO'
    f'\n{am}B) {br}CANADÁ'
    f'\n{am}C) {br}LÍBANO'
    f'\n{am}D) {br}MARROCOS',
    # Pergunta 17
    f'{fvm}>>>  A que país pertence a Groenlândia?   {sc}'
    f'\n{am}A) {br}DINAMARCA'
    f'\n{am}B) {br}INGLATERRA'
    f'\n{am}C) {br}NORUEGA'
    f'\n{am}D) {br}ESTADOS UNIDOS',
    # Pergunta 18
    f'{fvm}>>>  Qual foi o primeiro presidente do Brasil eleito pelo povo?   {sc}'
    f'\n{am}A) {br}GETÚLIO VARGAS'
    f'\n{am}B) {br}PRUDENTE DE MORAES'
    f'\n{am}C) {br}WASHINGTON LUÍS'
    f'\n{am}D) {br}TANCREDO NEVES',
    # Pergunta 19
    f'{fvm}>>>  Miró, Picasso e Salvador Dalí eram pintores:   {sc}'
    f'\n{am}A) {br}ITALIANOS'
    f'\n{am}B) {br}PORTUGUESES'
    f'\n{am}C) {br}ESPANHÓIS'
    f'\n{am}D) {br}CHILENOS'
],
    'resposta':['A', 'D', 'B', 'B', 'C', 'B', 'D', 'A', 'C', 'B', 'B', 'B', 'B', 'C', 'B', 'A', 'C', 'A', 'B', 'C']
}

nivel4 = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Que trópico atravessa o Saara?   {sc}'
    f'\n{am}A) {br}CAPRICÓRNIO'
    f'\n{am}B) {br}VIRGEM'
    f'\n{am}C) {br}CÂNCER'
    f'\n{am}D) {br}LEÃO',
    # Pergunta 1
    f'{fvm}>>>  “Guernica” é uma tela de qual pintor?   {sc}'
    f'\n{am}A) {br}MONET'
    f'\n{am}B) {br}RENDIR'
    f'\n{am}C) {br}PICASSO'
    f'\n{am}D) {br}LEONARDO DA VINCI',
    # Pergunta 2
    f'{fvm}>>>  Em que ano foi inaugurada a estátua do Cristo Redentor no Rio de Janeiro?   {sc}'
    f'\n{am}A) {br}1921'
    f'\n{am}B) {br}1931'
    f'\n{am}C) {br}1941'
    f'\n{am}D) {br}1951',
    # Pergunta 3
    f'{fvm}>>>  A que país deve-se viajar para subir o Monte Parnaso?   {sc}'
    f'\n{am}A) {br}ITÁLIA'
    f'\n{am}B) {br}FRANÇA'
    f'\n{am}C) {br}GRÉCIA'
    f'\n{am}D) {br}TURQUIA',
    # Pergunta 4
    f'{fvm}>>>  Qual destas palavras é sinônimo de cabal?   {sc}'
    f'\n{am}A) {br}BAIXO'
    f'\n{am}B) {br}PERFEITO'
    f'\n{am}C) {br}ATREVIDO'
    f'\n{am}D) {br}ENFERMO',
    # Pergunta 5
    f'{fvm}>>>  Qual foi a locomotiva a vapor que trafegou na Estrada de Ferro Mauá em 1854?   {sc}'
    f'\n{am}A) {br}SANTA-FÉ'
    f'\n{am}B) {br}LOCO-BREQUE'
    f'\n{am}C) {br}AMERICAN'
    f'\n{am}D) {br}BARONESA',
    # Pergunta 6
    f'{fvm}>>>  O que é palato?   {sc}'
    f'\n{am}A) {br}BARRIGA DA PERNA'
    f'\n{am}B) {br}MENINA DOS OLHOS'
    f'\n{am}C) {br}LÍNGUA'
    f'\n{am}D) {br}CÉU DA BOCA',
    # Pergunta 7
    f'{fvm}>>>  Qual atleta foi desclassificado por uso de doping nas Olimpíadas de 1988?   {sc}'
    f'\n{am}A) {br}MIKE POWELL'
    f'\n{am}B) {br}BEN JOHNSON'
    f'\n{am}C) {br}CARL LEWIS'
    f'\n{am}D) {br}LINFORD CHRISTIE',
    # Pergunta 8
    f'{fvm}>>>  Qual metal possui o símbolo Hg?   {sc}'
    f'\n{am}A) {br}FERRO'
    f'\n{am}B) {br}AÇO'
    f'\n{am}C) {br}MERCÚRIO'
    f'\n{am}D) {br}OURO',
    # Pergunta 9
    f'{fvm}>>>  Quem foi chamado de Águia de Haia?   {sc}'
    f'\n{am}A) {br}JORGE AMADO'
    f'\n{am}B) {br}EÇA DE QUEIROZ'
    f'\n{am}C) {br}RUI BARBOSA'
    f'\n{am}D) {br}RAIMUNDO CORRÊA',
    # Pergunta 10
    f'{fvm}>>>  O que procurava Juan Ponce de Leon quando descobriu a Flórida?   {sc}'
    f'\n{am}A) {br}A CIDADE PERDIDA DE OURO'
    f'\n{am}B) {br}A FONTE DA JUVENTUDE'
    f'\n{am}C) {br}UNICÓRNIOS'
    f'\n{am}D) {br}SEU GATO',
    # Pergunta 11
    f'{fvm}>>>  As Ilhas Malvinas também são chamadas de:   {sc}'
    f'\n{am}A) {br}STANLEY'
    f'\n{am}B) {br}WEDELLS'
    f'\n{am}C) {br}3 MEDANOSA'
    f'\n{am}D) {br}FALKLAND',
    # Pergunta 12
    f'{fvm}>>>  Qual destes países não se situa no Equador?   {sc}'
    f'\n{am}A) {br}QUÊNIA'
    f'\n{am}B) {br}EQUADOR'
    f'\n{am}C) {br}CHILE'
    f'\n{am}D) {br}INDONÉSIA',
    # Pergunta 13
    f'{fvm}>>>  Em que país Leonardo da Vinci viveu seus últimos dias?   {sc}'
    f'\n{am}A) {br}ESPANHA'
    f'\n{am}B) {br}HOLANDA'
    f'\n{am}C) {br}FRANÇA'
    f'\n{am}D) {br}ITÁLIA',
    # Pergunta 14
    f'{fvm}>>>  Pablo Picasso foi um dos criadores do:   {sc}'
    f'\n{am}A) {br}CUBISMO'
    f'\n{am}B) {br}SURREALISMO'
    f'\n{am}C) {br}IMPRESSIONISMO'
    f'\n{am}D) {br}REALISMO',
    # Pergunta 15
    f'{fvm}>>>  Como se chama o explorador de grutas e cavernas?   {sc}'
    f'\n{am}A) {br}ESPELEÓLOGO'
    f'\n{am}B) {br}AGROSTÓLOGO'
    f'\n{am}C) {br}PSICÓLOGO'
    f'\n{am}D) {br}CAMPANÓLOGO',
    # Pergunta 16
    f'{fvm}>>>  A baleia está classificada em qual grupo de mamíferos?   {sc}'
    f'\n{am}A) {br}CETÁCEOS'
    f'\n{am}B) {br}FELINOS'
    f'\n{am}C) {br}SIRÊNIOS'
    f'\n{am}D) {br}CARNÍVOROS',
    # Pergunta 17
    f'{fvm}>>>  O filme “A noviça rebelde”, premiado com 5 Oscars, foi estrelado por:   {sc}'
    f'\n{am}A) {br}JUDY GARLAND'
    f'\n{am}B) {br}SHIRLEY TEMPLE'
    f'\n{am}C) {br}JULIE ANDREWS'
    f'\n{am}D) {br}DORIS DAY',
    # Pergunta 18
    f'{fvm}>>>  O que o pintor Claude Monet representou em suas telas?   {sc}'
    f'\n{am}A) {br}OS JARDINS DE GIVERNY'
    f'\n{am}B) {br}OS BISTRÔS DE PARIS'
    f'\n{am}C) {br}CENAS DO MOULIN ROUGE'
    f'\n{am}D) {br}PAISAGENS DA PROVENÇA',
    # Pergunta 19
    f'{fvm}>>>  Como é chamada a gravura impressa sobre pranchas de madeira?   {sc}'
    f'\n{am}A) {br}MATEROGRAFIA'
    f'\n{am}B) {br}LITOGRAFIA'
    f'\n{am}C) {br}XILOGRAFIA'
    f'\n{am}D) {br}SERIGRAFIA',
],
    'resposta':['C', 'C', 'B', 'C', 'B', 'D', 'D', 'B', 'C', 'C', 'B', 'D', 'C', 'C', 'A', 'A', 'A', 'C', 'A', 'C']
}

# Foi criado esse dicionário para serem usadas quando o jogador quiser pular no jogo, assim evito a repetição;
pulos = {'pergunta': [
    # Pergunta 0
    f'{fvm}>>>  Qual personagem da turma da Mônica tem apenas cinco fios de cabelo?   {sc}'
    f'\n{am}A) {br}MÔNICA'
    f'\n{am}B) {br}CEBOLINHA'
    f'\n{am}C) {br}CASCÃO'
    f'\n{am}D) {br}MAGALI',
    # Pergunta 1
    f'{fvm}>>>  Qual cantora tinha o apelido de “Ternurinha” na época da jovem guarda?   {sc}'
    f'\n{am}A) {br}SILVINHA'
    f'\n{am}B) {br}WANDERLÉIA'
    f'\n{am}C) {br}GRETCHEN'
    f'\n{am}D) {br}MARTINHA',
    # Pergunta 2
    f'{fvm}>>>  Quantas dentições naturais tem o ser humano durante a vida?   {sc}'
    f'\n{am}A) {br}UMA'
    f'\n{am}B) {br}DUAS'
    f'\n{am}C) {br}TRÊS'
    f'\n{am}D) {br}QUATRO',
    # Pergunta 3
    f'{fvm}>>>  Quantos dias tem um ano bissexto?   {sc}'
    f'\n{am}A) {br}364'
    f'\n{am}B) {br}365'
    f'\n{am}C) {br}366'
    f'\n{am}D) {br}367',
    # Pergunta 4
    f'{fvm}>>>  Quem foi técnico da Seleção brasileira de futebol na Copa de 98?   {sc}'
    f'\n{am}A) {br}ZAGALLO'
    f'\n{am}B) {br}SCOLARI'
    f'\n{am}C) {br}LUXEMBURGO'
    f'\n{am}D) {br}CARPEGIANNI',
    # Pergunta 5
    f'{fvm}>>>  O dromedário tem quantas corcovas?   {sc}'
    f'\n{am}A) {br}UMA'
    f'\n{am}B) {br}DUAS'
    f'\n{am}C) {br}TRÊS'
    f'\n{am}D) {br}QUATRO',
    # Pergunta 6
    f'{fvm}>>>  Qual é a altura oficial do aro na cesta no basquete?   {sc}'
    f'\n{am}A) {br}3.05 METROS'
    f'\n{am}B) {br}2.97 METROS'
    f'\n{am}C) {br}3.10 METROS'
    f'\n{am}D) {br}3.00 METROS',
    # Pergunta 7
    f'{fvm}>>>  Quem foi aluno de Platão e tutor de Alexandre, o Grande?   {sc}'
    f'\n{am}A) {br}PITÁGORAS'
    f'\n{am}B) {br}DIDEROT'
    f'\n{am}C) {br}ARISTÓTELES'
    f'\n{am}D) {br}GALILEU GALILEI',
    # Pergunta 8
    f'{fvm}>>>  Onde estão os sepulcros de Michelangelo, Maquiavel e Galileu?   {sc}'
    f'\n{am}A) {br}MILÃO'
    f'\n{am}B) {br}FLORENÇA'
    f'\n{am}C) {br}VENEZA'
    f'\n{am}D) {br}GÊNOVA',
    # Pergunta 9
    f'{fvm}>>>  A que letra do nosso alfabeto corresponde a letra grega tau?   {sc}'
    f'\n{am}A) {br}LETRA F'
    f'\n{am}B) {br}LETRA H'
    f'\n{am}C) {br}LETRA J'
    f'\n{am}D) {br}LETRA T',
    # Pergunta 10
    f'{fvm}>>>  Em qual guerra lutou Paul Newman pela marinha americana?   {sc}'
    f'\n{am}A) {br}PRIMEIRA GUERRA MUNDIAL'
    f'\n{am}B) {br}GUERRA DO VIETNÃ'
    f'\n{am}C) {br}GUERRA DA CORÉIA'
    f'\n{am}D) {br}SEGUNDA GUERRA MUNDIAL',
    # Pergunta 11
    f'{fvm}>>>  Qual é o nome dado a um conjunto de sinos?   {sc}'
    f'\n{am}A) {br}CORRIMÃO'
    f'\n{am}B) {br}CARRILHÃO'
    f'\n{am}C) {br}BADALADA'
    f'\n{am}D) {br}CORSELETE',
    # Pergunta 12
    f'{fvm}>>>  Qual foi o último presidente militar do Brasil?   {sc}'
    f'\n{am}A) {br}FERNANDO COLLOR'
    f'\n{am}B) {br}JOÃO FIGUEIREDO'
    f'\n{am}C) {br}TANCREDO NEVES'
    f'\n{am}D) {br}JOÃO GOULART',
    # Pergunta 13
    f'{fvm}>>>  O trapézio é um músculo que está situado:   {sc}'
    f'\n{am}A) {br}NO PESCOÇO'
    f'\n{am}B) {br}NO OMBRO'
    f'\n{am}C) {br}NA CABEÇA'
    f'\n{am}D) {br}NO BRAÇO',
    # Pergunta 14
    f'{fvm}>>>  Quem escreveu o livro “A sangue frio” em 1966?   {sc}'
    f'\n{am}A) {br}TRUMAN CAPOTE'
    f'\n{am}B) {br}HENRY JAMES'
    f'\n{am}C) {br}JOHN STEINBECK'
    f'\n{am}D) {br}TONI MORRISON',
    # Pergunta 15
    f'{fvm}>>>  Quem escreveu “Ulisses” em 1922?   {sc}'
    f'\n{am}A) {br}ERNEST HEMINGWAY'
    f'\n{am}B) {br}MARCEL PROUST'
    f'\n{am}C) {br}T.S. ELLIOT'
    f'\n{am}D) {br}JAMES JOYCE',
],
    
    'resposta': ['B', 'B', 'B', 'C', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'B', 'B', 'B', 'A', 'D']
}


# Essa função faz com que o sorteio não se repita; Lembrando que a ordem do sorteio corresponde a ordem das perguntas;
sorteio = []

while len(sorteio) != len(nivel1['pergunta']):
    r = randint(0, len(nivel1['pergunta']) - 1)
    if r not in sorteio:
        sorteio.append(r)

# O mesmo ocorre para as perguntas da função pular;
pular = []
while len(pular) != len(pulos['pergunta']):
    r = randint(0, len(pulos['pergunta']) - 1)
    if r not in pular:
        pular.append(r)


# ===================== FUNÇÕES DE AUXILIO DAS PERGUNTAS DO JOGO ======================================================
def perguntas(pergunta, resposta, proxima, p):

    pergunta = pergunta
    resposta = resposta

    print(pergunta)
    linha()
    som('audio/frase_entendeu.mp3')
    while True:
        som('audio/frase_respondemos.mp3')
        escolha = str(input(f'VOCÊ VAI RESPONDER OU PEDIR AJUDA? {am}[R/A]{br}: ')).upper().strip()[0]
        linha()
        if escolha == 'R':
            confirmacao(pergunta, resposta, proxima, premio)
        elif escolha == 'A':
            menu_ajuda(pergunta, resposta, proxima, p)
        else:
            erro(f'ERRO! Dados inválidos, digite apenas {am}R{br} ou {am}A{br}.')


def pula(pergunta, resposta, proxima, p):
    global pulo
    
    if pulo > 0:
        pulo -= 1
        som('audio/frase_pular.mp3')
    
        pergunta = pulos['pergunta'][pular[p]]
        resposta = pulos['resposta'][pular[p]]
    
        print(pergunta)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)
    else:
        erro('Você já pulou 3 vezes. Você não tem mais essa opção!')
        menu_ajuda(pergunta, resposta, proxima, p)


def colegas(pergunta, resposta, proxima, p):
    global colega

    if colega > 0:
        colega -= 1
        pergunta = pergunta
        resposta = resposta

        opcoes = ['A', 'B', 'C', 'D']
        lista = []
        for pos, v in enumerate(opcoes):
            if resposta != v:
                lista.append(v)

        som('audio/frase_dificil_ajuda.mp3')
        som('audio/frase_colegas.mp3')
        print('A escolha dos nossos colegas são: Opção ', end='')
        for pos, v in enumerate(lista):
            print(f'- {vm}{v}{br} {pos +1}0%', end=' ')
            sleep(1)
        print(f'- {am}{resposta}{br} 40%')

        sleep(1)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)

    else:
        erro('Você já usou essa opção de ajuda!')
        menu_ajuda(pergunta, resposta, proxima, p)


def convidados(pergunta, resposta, proxima, p):
    global convidado

    if convidado > 0:
        convidado -= 1
        pergunta = pergunta
        resposta = resposta

        opcoes = ['A', 'B', 'C', 'D']
        lista = []
        for pos, v in enumerate(opcoes):
            if resposta != v:
                lista.append(v)

        som('audio/frase_dificil_ajuda.mp3')
        som('audio/frase_convidados.mp3')
        print('Escolha dos convidados: ', end='')

        for c in range(1, 4):
            print(f'{c}ª convidado: ', end='')
            if c < 3:
                print(f'{am}{resposta}{br} |', end=' ')
                sleep(1)
            else:
                print(f'{vm}{lista[0]}{br}')

        sleep(1)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)

    else:
        erro('Você já usou essa opção de ajuda!')
        menu_ajuda(pergunta, resposta, proxima, p)


def cartas(pergunta, resposta, proxima, p):
    global carta
    
    if carta > 0:
        carta -= 1
        pergunta = pergunta
        resposta = resposta

        opcoes = ['A', 'B', 'C', 'D']
        lista = []
        for pos, v in enumerate(opcoes):
            if resposta != v:
                lista.append(v)
    
        som('audio/frase_cartas.mp3')
        excluir = randint(1, 3)
    
        print(f'Você tirou um {excluir} !', end=' ')
        sleep(1)
        if excluir == 1:
            print('Que pena, você ainda tem 3 opções!')
        elif excluir == 2:
            print('Boa! só resta 2 opções agora.')
        elif excluir == 3:
            print('Parabéns! Agora ficou fácil...')
    
        print('Desconsidere as opções:', end=' ')
        print(f'{vm}{lista[-3: -0 + excluir]}{br}')
    
        sleep(1)
        linha()
        confirmacao(pergunta, resposta, proxima, premio)
    else:
        erro('Você já usou essa opção de ajuda!')
        menu_ajuda(pergunta, resposta, proxima, p)
        

def confirmacao(pergunta, resposta, proxima, premio):
    while True:
        som('audio/frase_pergunta_certa.mp3')
        resp = str(input(f'{am}QUAL A RESPOSTA CERTA?{br} ')).upper().strip()[0]
        if resp in 'ABCD':
            linha()
            
            while True:
                som('audio/frase_pergunta.mp3')
                resp2 = str(input(f'VOCÊ ESTÁ CERTO DISSO, POSSO PERGUNTAR? {am}[S/N]{br}: ')).upper().strip()[0]
                linha()
                if resp2 == 'S':
                    if resp == resposta:
                        som('audio/frase_parabens.mp3')
                        print(f'{am}CERTA RESPOSTA!{br}')
                        som('audio/frase_acerto.mp3')
        
                        stop(arq, nome, premio)
                        if pulo == 3 and carta == 1 and convidado == 1 and colega == 1:
                            som('audio/frase2.mp3')
                            som('audio/frase1.mp3')
                        proxima()
                    else:
                        som('audio/frase_erro.mp3')
                        print(f'{vm}QUE PENA, VOCÊ ERROU!{br}')
                        premio = errar
                        final(arq, nome, premio)
                        break
                elif resp2 == 'N':
                    continue
                else:
                    erro(f'ERRO! dados inválidos, digite apenas {am}S{br} ou {am}N{br}.')
                
        else:
            erro(f'ERRO! Dados inválidos, digite apenas as opções {am}A B C D{br}')


def menu_ajuda(pergunta, resposta, proxima, p):
    som('audio/frase_ajuda1.mp3')
    print(f'{rx}A) {br}PULAR')
    print(f'{rx}B) {br}CARTAS')
    print(f'{rx}C) {br}CONVIDADOS')
    print(f'{rx}D) {br}COLEGAS')
    linha()
    som('audio/frase_opcoes.mp3')
    while True:
        som('audio/frase_ajuda2.mp3')
        resp = str(input('E PARA QUEM VOCÊ VAI PEDIR AJUDA? ')).upper().strip()[0]
        linha()
        if resp == 'A':
            pula(pergunta, resposta, proxima, p)
        elif resp == 'B':
            cartas(pergunta, resposta, proxima, p)
        elif resp == 'C':
            convidados(pergunta, resposta, proxima, p)
        elif resp == 'D':
            colegas(pergunta, resposta, proxima, p)
        else:
            erro('ERRO! Dados inválidos, digite apenas as opções do menu.')


# ===================== PERGUNTAS DO JOGO =============================================================================
def rodada1():
    """
    P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
        será escolhida.
    pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
        indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
        repetem, isso é feito na variável sorteio em variáveis globais).
    resposta: Ocorre o mesmo que na pergunta.
    cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
        chamada moeda, apenas para converter inteiro para o formato dinheiro.
    SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
        aúdio está.
    :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
        posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
        rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
        recurso da ajuda pular.
    """
    global premio, acerto, errar, parar, p
    acerto = valor[0]
    p = 0
    pergunta = nivel1['pergunta'][sorteio[0]]
    resposta = nivel1['resposta'][sorteio[0]]
    cabecalho(f' 1ª PERGUNTA, VALENDO {valor[0]} REAIS')
    placar()
    som('audio/frase_1mil.mp3')
    perguntas(pergunta, resposta, rodada2, p)


def rodada2():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[1]
    parar = valor[0]
    p = 1
    pergunta = nivel1['pergunta'][sorteio[1]]
    resposta = nivel1['resposta'][sorteio[1]]
    cabecalho(f' 2ª PERGUNTA, VALENDO {valor[1]} REAIS')
    placar()
    som('audio/frase_2mil.mp3')
    perguntas(pergunta, resposta, rodada3, p)


def rodada3():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[2]
    parar = valor[1]
    errar = valor[0]
    p = 2
    pergunta = nivel1['pergunta'][sorteio[2]]
    resposta = nivel1['resposta'][sorteio[2]]
    cabecalho(f' 3ª PERGUNTA, VALENDO {valor[2]} REAIS')
    placar()
    som('audio/frase_3mil.mp3')
    perguntas(pergunta, resposta, rodada4, p)


def rodada4():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[3]
    parar = valor[2]
    errar = valor[1]
    p = 3
    pergunta = nivel1['pergunta'][sorteio[3]]
    resposta = nivel1['resposta'][sorteio[3]]
    cabecalho(f' 4ª PERGUNTA, VALENDO {valor[3]} REAIS')
    placar()
    som('audio/frase_4mil.mp3')
    perguntas(pergunta, resposta, rodada5, p)


def rodada5():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[4]
    parar = valor[3]
    errar = valor[2]
    p = 4
    pergunta = nivel1['pergunta'][sorteio[4]]
    resposta = nivel1['resposta'][sorteio[4]]
    cabecalho(f' 5ª PERGUNTA, VALENDO {valor[4]} REAIS')
    placar()
    som('audio/frase_5mil.mp3')
    perguntas(pergunta, resposta, rodada6, p)


def rodada6():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[5]
    parar = valor[4]
    errar = valor[3]
    p = 5
    pergunta = nivel2['pergunta'][sorteio[0]]
    resposta = nivel2['resposta'][sorteio[0]]
    cabecalho(f' 6ª PERGUNTA, VALENDO {valor[5]} REAIS')
    placar()
    som('audio/frase_10mil.mp3')
    perguntas(pergunta, resposta, rodada7, p)


def rodada7():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[6]
    parar = valor[5]
    errar = valor[4]
    p = 6
    pergunta = nivel2['pergunta'][sorteio[1]]
    resposta = nivel2['resposta'][sorteio[1]]
    cabecalho(f' 7ª PERGUNTA, VALENDO {valor[6]} REAIS')
    placar()
    som('audio/frase_20mil.mp3')
    perguntas(pergunta, resposta, rodada8, p)


def rodada8():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[7]
    parar = valor[6]
    errar = valor[5]
    p = 7
    pergunta = nivel2['pergunta'][sorteio[2]]
    resposta = nivel2['resposta'][sorteio[2]]
    cabecalho(f' 8ª PERGUNTA, VALENDO {valor[7]} REAIS')
    placar()
    som('audio/frase_30mil.mp3')
    perguntas(pergunta, resposta, rodada9, p)


def rodada9():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[8]
    parar = valor[7]
    errar = valor[6]
    p = 8
    pergunta = nivel2['pergunta'][sorteio[3]]
    resposta = nivel2['resposta'][sorteio[3]]
    cabecalho(f' 9ª PERGUNTA, VALENDO {valor[8]} REAIS')
    placar()
    som('audio/frase_40mil.mp3')
    perguntas(pergunta, resposta, rodada10, p)


def rodada10():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[9]
    parar = valor[8]
    errar = valor[7]
    p = 9
    pergunta = nivel2['pergunta'][sorteio[4]]
    resposta = nivel2['resposta'][sorteio[4]]
    cabecalho(f' 10ª PERGUNTA, VALENDO {valor[9]} REAIS')
    placar()
    som('audio/frase_50mil.mp3')
    perguntas(pergunta, resposta, rodada11, p)


def rodada11():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[10]
    parar = valor[9]
    errar = valor[8]
    p = 10
    pergunta = nivel3['pergunta'][sorteio[0]]
    resposta = nivel3['resposta'][sorteio[0]]
    cabecalho(f' 11ª PERGUNTA, VALENDO {valor[10]} REAIS')
    placar()
    som('audio/frase_100mil.mp3')
    perguntas(pergunta, resposta, rodada12, p)


def rodada12():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[11]
    parar = valor[10]
    errar = valor[9]
    p = 11
    pergunta = nivel3['pergunta'][sorteio[1]]
    resposta = nivel3['resposta'][sorteio[1]]
    cabecalho(f' 12ª PERGUNTA, VALENDO {valor[11]} REAIS')
    placar()
    som('audio/frase_200mil.mp3')
    perguntas(pergunta, resposta, rodada13, p)


def rodada13():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[12]
    parar = valor[11]
    errar = valor[10]
    p = 12
    pergunta = nivel3['pergunta'][sorteio[2]]
    resposta = nivel3['resposta'][sorteio[2]]
    cabecalho(f' 13ª PERGUNTA, VALENDO {valor[12]} REAIS')
    placar()
    som('audio/frase_300mil.mp3')
    perguntas(pergunta, resposta, rodada14, p)


def rodada14():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[13]
    parar = valor[12]
    errar = valor[11]
    p = 13
    pergunta = nivel3['pergunta'][sorteio[3]]
    resposta = nivel3['resposta'][sorteio[3]]
    cabecalho(f' 14ª PERGUNTA, VALENDO {valor[13]} REAIS')
    placar()
    som('audio/frase_400mil.mp3')
    perguntas(pergunta, resposta, rodada15, p)


def rodada15():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p
    acerto = valor[14]
    parar = valor[13]
    errar = valor[12]
    p = 14
    pergunta = nivel3['pergunta'][sorteio[4]]
    resposta = nivel3['resposta'][sorteio[4]]
    cabecalho(f' 15ª PERGUNTA, VALENDO {valor[14]} REAIS')
    placar()
    som('audio/frase_500mil.mp3')
    perguntas(pergunta, resposta, rodada16, p)


def rodada16():
    """
        P: é a definição para o indice que será usado caso o usuário use a ajuda do pulo. Ele define qual a pergunta que
            será escolhida.
        pergunta: É definido o nivel, a variável sorteio faz a escolha da pergunta e após essa escolha é selecionada o
            indice 0 (Lembrando que o sorteio é feito uma vez de forma que não aja números iguais, assim as perguntas não se
            repetem, isso é feito na variável sorteio em variáveis globais).
        resposta: Ocorre o mesmo que na pergunta.
        cabecalho: Dentro da função é colocado a variável valor (definida em variáveis globais) dentro de outra função
            chamada moeda, apenas para converter inteiro para o formato dinheiro.
        SOM: A função som usa os recursos da bibliotéca pygame. Ela recebe o parâmetro que apenas indica o caminho que o
            aúdio está.
        :return: O retorno indica a função perguntas, recebeno como parâmetro a pergunta e resposta, assim a cada rodada
            posso ter o controle para que não se repitam definindo o indice. Também recebe o parâmetro que define a próxima
            rodada. E por fim recebe o valor da variável P que ira definir o indice das perguntas caso o usuário use o
            recurso da ajuda pular.
        """
    global premio, acerto, errar, parar, p, pulo, carta, convidado, colega
    acerto = valor[15]
    parar = errar = pulo = carta = convidado = colega = 0
    p = 15
    pergunta = nivel4['pergunta'][sorteio[0]]
    resposta = nivel4['resposta'][sorteio[0]]
    cabecalho(f' PERGUNTA FINAL, VALENDO {valor[15]} REAIS')
    placar()
    som('audio/frase_final.mp3')
    perguntas(pergunta, resposta, final, p)


# ===================== FUNÇÕES DO JOGO ===============================================================================
def inicio():
    # Função para definir o nome do arquivo aonde os dados dos jogadores ficarão salvos.
    if not arquivoexiste(arq):
        criararquivo(arq)

    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura.mp3')
    pygame.mixer.music.play()
    layout()
    sleep(5)
    menu()


def cadastro():
    global nome
    som('audio/frase_participante.mp3')
    cabecalho('CADASTRO DO JOGADOR')
    nome = str(input('Nome do jogador: ')).title().strip()
    linha()
    print(f'{"Seja bem vindo(a) "f"{am}{nome}{br} começa agora o jogo "f"{am}SHOW DO MILHÃO!{br}"}')
    linha()
    while True:
        som('audio/frase_inicio.mp3')
        resp = str(input('VAMOS JOGAR? [S/N]: ')).upper().strip()[0]
        linha()
        if resp == 'S':
            rodada1()
        elif resp == 'N':
            cabecalho('MENU DO JOGO')
            menu()
        else:
            erro(f'ERRO! Dados inválidos. Digite apenas {am}S{br} ou {am}N{br}.')


def menu():
    print(f'{am}A) {br}COMEÇAR NOVO JOGO')
    print(f'{am}B) {br}RANKING DOS JOGADORES')
    print(f'{am}C) {br}MANUAL DO JOGO')
    print(f'{am}D) {br}SAIR DO JOGO')
    linha()
    while True:
        resp = str(input('ESCOLHA A OPÇÃO DESEJADA: ')).strip().upper()[0]
        if resp == 'A':
            cadastro()
        elif resp == 'B':
            som('audio/frase_lombardi.mp3')
            ranking(arq)
        elif resp == 'C':
            som('audio/frase_lombardi.mp3')
            print('Regras do jogo') #regras()
        elif resp == 'D':
            sair()
            break
        else:
            erro('ERRO! Dados inválidos, digite as opções do menu!')


def sair():
    som('audio/frase_tchau.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura_continuacao.mp3')
    pygame.mixer.music.play()
    linha()
    print('Saindo do jogo', end='')
    sleep(.5)
    for c in range(1, 48):
        print('.', end='')
        sleep(.5)
    #sleep(1)
    print(f'.....{am}Até a próxima!')
    
    
def stop(arq, nome, premio):
    linha()
    while True:
        resp = str(input(f'VOCÊ QUER CONTINUAR? {am}[S/N]{br} ')).upper().strip()[0]
        linha()
        if resp == 'N':
            som('audio/frase_parar.mp3')
            resp2 = str(input(f'ESTÁ CERTO DISSO? {am}[S/N]{br}: ')).upper().strip()[0]
            linha()
            if resp2 == 'S':
                premio = parar
                final(arq, nome, premio)
        elif resp == 'S':
            break
        else:
            erro(f'ERRO! Dados inválidos, digite apenas {am}S{br} ou {am}N{br}!')


def final(arq, nome, premio):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        som('audio/frase_lombardi.mp3')
        cabecalho('RESULTADO DA PARTIDA')
        print(f'| {am}{"JOGADOR":^37}{br} | {am}{"PREMIAÇÃO":^36}{br} |')
        linha()
        print(f'| {nome:^37} | {premio:^36} |')
        linha()
        try:
            a.write(f'{nome};{premio}\n')
        except:
            print(f'ERRO ao cadastrar o jogador {nome}')
        else:
            #print(f'Novo registro de {nome} adicionado.')
            a.close()
            sair()
    

def ranking(arq):
    pygame.mixer.init()
    pygame.mixer.music.load('audio/abertura_continuacao.mp3')
    pygame.mixer.music.play()
    try:
        a = open(arq, 'rt')
    except:
        print(f'Houve um ERRO na abertura do aquivo!')
    else:
        cabecalho('HANKING DOS JOGADORES')
        print(f'| {am}{"JOGADOR":^37}{br} | {am}{"PREMIAÇÃO":^36}{br} |')
        linha()
        for dados in a:
            dado = dados.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'| {dado[0]:^37} | {dado[1]:^36} |')
            linha()
            sleep(.5)
    finally:
        a.close()
        menu()
        
# ===================== FUNÇÕES DO SISTEMA ============================================================================
def layout():
    print(br)
    linha('=')
    print(f'|{am+"JOGO SHOW DO MILHÃO - V1.0".center(98)+br}|')
    linha('=')
    print(f'|               {am}{"BEM VINDO AO"} {br}{"JOGO SHOW DO MILHÃO"} {am}{" - DESENVOLVIDO POR "}  '
          f'{br}{"DARLAN ARAUJO"}               |')
    linha('=')
    print(f'|              {az}{"Acerte as perguntas e concorra ao premio de"} {vm}{"R$ 1.000,000,00"} '
          f'{az}{"de reais"}{br}                |')
    linha('=')
    

def placar():
    print(f'|  {am}{"  AJUDAS DO JOGO >>>  "}{br} |  {"PULAR: "}  {am}{pulo}{br}   |  {"CARTAS: "}  {am}{carta}{br}   |'
          f'  {"CONVIDADOS: "}  {am}{convidado}{br}   |  {"COLEGAS: "}  {am}{colega}{br}    |')
    linha('=')
    print(f'| {am}{"PLACAR >>>"}{br} | {"ERRAR:"} {vm}{errar:<17}{br} |'
          f' {"PARAR:"} {rx}{parar:<19}{br} | {"ACERTO:"} {am}{acerto:<19}{br} |')
    linha('=')


def cabecalho(msg):
    print(br)
    linha('=')
    print(f'|{am}{msg.center(98)}{br}|')
    linha('=')


def som(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy()): pass


def linha(caractere='-', tam=100):
    print(caractere * tam)


def erro(msg):
    linha()
    print(f'{vm}{msg}{br}')
    linha()


def moeda(premio, moeda='R$ '):
    return f'{moeda}{premio:.2f}'.replace('.', ',')


def tempo():
    temp = 'on'
    print('TEMPO: ', end='')
    for c in range(1, 31):
        print(f'{c}', end=' ')
        sleep(1)
    temp = 'off'

    if temp == 'off':
        som('audio/frase_acabou_tempo.mp3')
        print('Que pena seu tempo acabou')
        final(arq, nome, premio)

# ===================== CRIAÇÃO DO ARQUIVO PARA SALVAR DADOS ==========================================================
def criararquivo(arq):
    # Função que cria o arquivo (banco de dados) caso não exista.
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo {arq}')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def arquivoexiste(arq):
    # Função que verifica se o arquivo (banco de dados) existe.
    try:
        a = open(arq, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


# ===================== INÍCIO DO PROGRAMA ============================================================================
inicio()

