"""A confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master"""

idade = int(input('Qual a idade do atleta: '))
if idade <= 9:
    print('Categoria Mirim.')
elif 9 < idade <= 14:
    print('Categoria Infantil.')
elif 14 < idade <= 19:
    print('Categoria Junior.')
elif 19 < idade <= 20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')
