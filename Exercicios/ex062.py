'''
DESAFIO 062

Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos
o programa ENCERRA QUANDO ELE DISSER que quer MOSTRAR 0 TERMOS.

'''

primeiro = int(input('Digite o TERMO: '))
razao = int(input('Digite a RAZÃO: '))

termo = primeiro
contador = 1

total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end= '')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja acrescentar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))