"""Desenvolva um programa que leia seis números inteiros e a soma apenas
 daqueles que forem pares. Se o valor digitado for impar, desconsidere-o"""

n = [int(input('digite um numero ')), int(input('digite um numero ')), int(input('digite um numero ')),
     int(input('digite um numero ')), int(input('digite um numero ')), int(input('digite um numero '))]
s = 0
pares = ''
for i in range(0, len(n)):
    if n[i] % 2 == 0:
        s += n[i]
        pares += str(' {}'.format(n[i]))
print('Os números pares são:{}. E a soma deles é {}.'.format(pares, s))