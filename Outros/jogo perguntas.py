import random



numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numero = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
texto = {1: ['davi', 'darlan', 'carol', 'silvana', 'luana', 'tania', 'vilma']}

n1 = random.randint(0, len(numero) -1)
n2 = random.randint(0, len(texto))
n3 = (texto[1][n2])

print('DESAFIO VOCÊ A ADIVINHAR O NÚMERO QUE ESTOU PENSANDO. VOCÊ TEM 3 TENTATIVAS.')
print(n3)
for comando in range(4, 0, -1):
    resposta = int(input(('DE 0 A 10 QUAL É O NÚMERO? ')))
    if resposta < n1:
        print('VOCÊ ERROU! TENTE UM NÚMERO MAIOR.')
    elif resposta > n1:
        print('VOCÊ ERROU! TENTE UM NÚMERO MAIS BAIXO.')
    elif resposta == n1:
        print('PARABÉNS! VOCÊ ACERTOU')
        print('O NÚMERO QUE PESEI ERA: {}'.format(n1))
        break

    print('QUE PENA. VOCÊ NÃO CONSEGUIU. O NÚMERO ERA: {}'.format(n1))