time = ('santos', 'vasco', 'flamengo')

print(time.count('santos'))
num = int(input('Qual a posição da tabela: '))
print(len(time[num]))
'''while True:
    num = int(input('Qual a posição da tabela: '))
    print(time[num])

    resp = str(input('Deseja consultar outro time? [S/N]: ')).upper().strip()[0]
    if resp == 'S':
        print()
    else:
        print('Fim do programa!')
        break'''
