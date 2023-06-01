"""Crie um programa que faça o computador jogar Jokenpô com você"""

from random import choice
from time import sleep
pc = ['PEDRA', 'PAPEL', 'TESOURA']
res = choice(pc)

print('|' * 51)
print('|' * 14, '    J O K E N P Ô    ', '|' * 14)
print('|' * 51)
valor = str(input('''VAMOS JOGAR! ESCOLHA
PEDRA, PAPEL OU TESOURA
ADIVINHE O QUE COLOQUEI: ''')).upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if valor == res:
    print('Eu coloquei {} e você {}.\nEMPATAMOS!!'.format(res, valor))
elif res == 'PAPEL' and valor == 'PEDRA' or res == 'TESOURA' and valor == 'PAPEL' or res == \
        'PEDRA' and valor == 'TESOURA':
    print('Eu coloquei {} e você {}.\nVOCÊ PERDEU!!'.format(res, valor))
elif valor == 'PAPEL' and res == 'PEDRA' or valor == 'TESOURA' and res == 'PAPEL' or valor == \
     'PEDRA' and res == 'TESOURA':
    print('Eu coloquei {} e você {}.\nVOCÊ GANHOU!!'.format(res, valor))
else:
    print('Não existe {}. Jogue novamente.'.format(valor))
