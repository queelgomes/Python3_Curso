"""Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date

total = [int(input('Qual o ano de nascimento da primeira pessoa: ')), \
    int(input('Qual o ano de nascimento da segunda pessoa: '))]
'''    int(input('Qual o ano de nascimento da terceira pessoa: ')), \
    int(input('Qual o ano de nascimento da quarta pessoa: ')), \
    int(input('Qual o ano de nascimento da quinta pessoa: ')), \
    int(input('Qual o ano de nascimento da sexta pessoa: ')), \
    int(input('Qual o ano de nascimento da sétima pessoa: '))'''
atual = date.today().year
maiores = 0
menores = 0
for i in range(0, 8):
    print(i)
    if atual - total[i] < 18:
        maiores += 1
    else:
        menores += 1
print('Temos {} maiores de idade e {} menores de idade.'.format(maiores, menores))