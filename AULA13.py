a = int(input('Escolha o primeiro número: '))
b = int(input('Escolha o ultimo número '))
c = int(input('Você quer pular a contagem de quantos em quantos números? '))
if a > b:
    c = c - c - c
    b -= 2
    for d in range(a, b + 1, c):
        print(d)
