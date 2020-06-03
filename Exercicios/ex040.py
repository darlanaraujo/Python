'''
DESAFIO 040

Crie um programa que LEIA DUAS NOTAS de um aluno e CALCULE SUA MÉDIA,
mostrando uma MENSAGEM NO FINAL de acordo com a média atingida:

MÉDIA ABAIXO DE 5.0: REPROVADO
MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
MÉDIA 7.0 OU SUPERIOR: APROVADO
'''

#Início do programa
print('#'*180)
print('#'*180)
print('{:^180}'.format('\033[1;33mSISTEMA PARA CALCULO DE MÉDIA DOS ALUNOS\033[m'))
print()
print('\033[1;36mINFORME ABAIXO AS DUAS NOTAS DO ALUNO PARA SABER A SUA MÉDIA FINAL. SABENDO QUE A MÉDIA NECESSÁRIA')
print('PARA PASSAR DIRETO É 7.0 OU SUPERIOR')
print()
nome = str(input('\033[1;30mNOME DO ALUNO: ')).upper().strip()
print('='*50)
n1 = float(input('INFORME A PRIMEIRA NOTA: '))
print('='*50)
n2 = float(input('INFORME A SEGUNDA NOTA: '))
print()
print('='*180)
print('='*180)
print('{:^180}'.format('\033[1;33mINFORMAÇÕES DO ALUNO\033[m'))
print()
print('\033[1;30mNOME DO ALUNO:\033[1;33m {}\033[30m'.format(nome))
print('='*50)
print('\033[1;30mPRIMEIRA NOTA:\033[1;33m {}'.format(n1))
print('\033[1;30mSEGUNDA NOTA:\033[1;33m {}\033[30m'.format(n2))
print('='*50)
media = (n1 + n2) / 2
print('\033[1;30mA MÉDIA DESSE SEMESTRE FOI:\033[33m {}\033[30m'.format(media))
print('='*180)
if media < 5.0:
    print('{:^180}'.format('\033[1;31mREPROVADO!\033[m'))
    print('\033[1;30mINFELIZMENTE O ALUNO \033[1;32m{} \033[1;30mNÃO CONSEGUIU A MÉDIA NECESSÁRIA PARA O SEMESTRE.'.format(nome))
elif media == 5.0 or media < 6.9:
    print('{:^180}'.format('\033[1;33mEM RECUPERAÇÃO!\033[m'))
    print('\033[1;30mA MÉDIA DO ALUNO \033[1;32m{} \033[1;30mNÃO FOI SUFICIENTE PARA PASSAR DIRETO.'.format(nome))
elif media >= 7.0:
    print('{:^180}'.format('\033[1;32mAPROVADO!\033[m'))
    print('\033[1;33mPARABÉNS! \033[1;30mO ALUNO \033[1;32m{} \033[1;30mCONSEGUIU A MÉDIA NECESSÁRIA PARA ESSE SEMESTRE.'.format(nome))
print()
print('='*180)
print('{:^180}'.format('FIM DO PROGRAMA!'))
print('#'*180)
print('#'*180)