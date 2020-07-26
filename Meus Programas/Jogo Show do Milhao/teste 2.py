pulo = 3
cartas = convidados = colegas = 1
    

def placar():
    print(f'| {" AJUDAS DO JOGO >>> "} | {"PULAR: "} {pulo} | {"CARTAS: "} {cartas} | {"CONVIDADOS: "} {convidados} | {"COLEGAS: "} {colegas} |')
    

def teste():
    global pulo
    placar()
    pulo -= 1
    placar()
    

teste()
placar()