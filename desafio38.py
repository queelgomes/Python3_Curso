"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print('O primeiro valor é maior.')
elif numero2 > numero1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
