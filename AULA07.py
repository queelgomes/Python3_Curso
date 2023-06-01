#desafio 5
n1 = int(input('Digite um número: '))
print('O número sucessor é {} e o antecessor é {}'.format((n1+1), (n1-1)))

#desafio 6
n2 = int(input('Digite outro número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format(n2, (n2*2), (n2*3), (n2**(1/2))))

#desafio 7
n3 = float(input('Qual foi a sua nota de português? '))
n4 = float(input('E qual foi sua nota de matemática? '))
print('Sua nota de matemática foi {} e de português {}. Sua média é {:.1f}.'.format(n4, n3, ((n3+n4)/2)))

#desafio 8
n5 = float(input('Escreva aqui a medida em metros:'))
n5_1 = n5*100
n5_2 = n5*1000
print('{}m tem {:.0f}cm e {:.0f}mm.'.format(n5, n5_1, n5_2))

#desafio 9
n6 = int(input('Você quer a tabuada de qual número? '))
print('='*10)
print('A tabuada do {} é: \n{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}'.format(n6, n6, (n6*0), n6, (n6*1), n6,  (n6*2), n6, (n6*3), n6, (n6*4)))
print('{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}'.format(n6, (n6*5), n6, (n6*6), n6, (n6*7), n6, (n6*8), n6, (n6*9)))
print('='*10)

#desafio 10
n7 = float(input('Quantos R$ você tem na carteira? '))
dolar = 3.27
print('Você consegue comprar U${:.2f} com R${:.2f}. Cotação do dolar hoje: R${:.2f}.'.format((n7/dolar), n7, dolar))

#desafio 11
n8 = float(input('Digite a altura da sua parede (em metros): '))
n9 = float(input('Digite a largura da sua parede (em metros): '))
area = n8*n9
tinta = area/2
print('Sua parede tem {} m2. Você precisa de {:.0f} litros de tinta.'.format(area, tinta))

#desafio 12
n10 = float(input('Preço atual: R$'))
com_desconto = n10-(n10*0.05)
print('Seu desconto foi de R${:.2f}. Você irá pagar R${:.2f}.'.format((n10*0.05), com_desconto))

#desafio13
n11 = float(input('Digite o seu salário: R$'))
aumento = float(input('Seu aumento será de: '))
salario_atual = n11+(n11*(aumento/100))
print(n11)
print(aumento)
print(salario_atual)
print('Você teve um aumento de {} %. Seu novo salário é R${:.2f}.'.format(aumento, salario_atual))
