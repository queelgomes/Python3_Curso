"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou passou do prazo."""

from datetime import date
nasceu = int(input('Qual seu ano de nascimento: '))
ano_atual = date.today().year
calculo = ano_atual - nasceu
if calculo == 18:
    print('Está na hora de se alistar. Procure o exército.')
elif calculo <= 17:
    print('Ainda não está no prazo de se alistar. Faltam {} anos.'.format(18 - calculo))
else:
    print('Já passou do prazo a {} anos. Se não se alistou, regularize.'.format(calculo - 18))
