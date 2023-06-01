"""import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.3}.'.format(num, raiz))"""

"""import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {}.'.format(num, math.trunc(raiz)))
# Aqui arrendamos para cima a raiz quadrada com o ceil."""

# desafio 16
"""n0 = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n0, math.floor(n0)))"""

# desafio 019
"""from random import choice
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')
lista = [n1, n2, n3, n4]
res = choice(lista)
print('O aluno escolhido foi o {}.'.format(res))"""

# desafio20
from random import shuffle
n5 = str(input('Digite o nome do aluno: '))
n6 = str(input('Digite o nome do aluno: '))
n7 = str(input('Digite o nome do aluno: '))
n8 = str(input('Digite o nome do aluno: '))
lista = [n5, n6, n7, n8]
shuffle(lista)  # Aqui a gente mistura a lista antes de dar o comando print.
print('A ordem dos alunos será: {}.'.format(lista))
