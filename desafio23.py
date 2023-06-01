numero = int(input('Digite um número de 0 a 9999s: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('''Analisando o número: {}:
Unidade:{}
Dezena:{}
Centena:{}
Milhar:{}'''.format(numero, unidade, dezena, centena, milhar))
