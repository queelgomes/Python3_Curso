"""Faça um programa que leia um número inteiro e diga se ele é ou não um núm primo"""

num = 3

for i in range(0, num + 1):
    for n in range(0, num + 1):
        print(n)
        print(i)
        if n % i == 0 and i == n:
            print('é um número primo. {} e {}'.format(n, i))
        else:
            print('Não é um número primo.{} e {}'.format(n, i))
