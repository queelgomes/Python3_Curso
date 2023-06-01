"""Escreva um programa que leia umnúmero inteiro qualquer e peça para o usuário escolher qual será a
base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""

num = int(input('Escolha um número: '))
print('''Você quer transformar esse valor em:
[ 1 ] binário
[ 2 ] octal
[ 3 ] hexadecimal''')
opção = int(input('Digite a sua opção: '))
if opção == 1:
    print('O numero {} em binário é {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')
