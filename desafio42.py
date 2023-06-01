"""Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
- equilatero: todos os lados iguais
- isosceles: dois lados são iguais
 - escaleno: todos os lados sao diferentes"""

r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida:'))
r3 = float(input('Digite a terceira medida: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Isso é um Triângulo Isósceles.')
    elif r1 != r2 or r2 != r3 or r3 != r1:
        print('Isso é um Triângulo Escaleno')
    elif r1 == r2 == r3:
        print('Isso é um Triangulo Equilátero.')
else:
    print('Isso não é um triângulo')