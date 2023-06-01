"""Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio,
indo de 10 até 0 com uma pausa de 1 segundo entre eles."""

from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("+'" * 14)
print("+' \033[0;33mFOGOS DE ARTIFÍCIOS!!!\033[m +'")
print("+'" * 14)