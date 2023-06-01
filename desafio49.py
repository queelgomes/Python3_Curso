"""Refaça o desafio 009, mostrando a tabuada de um número que o
 usuário escolher, só que agora utilizando um laço for"""

num = int(input('Você quer a tabuada do: '))
print('[' * 3, ' ESSA É A TABUADA DO {} '.format(num), ']' * 3)
for i in range(0, 10):
    print(' ' * 8, num,'x', i, '=', '\033[2;33m{}\033[m'.format(num * i))
