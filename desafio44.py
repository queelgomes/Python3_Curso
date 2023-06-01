"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- em ate 2x no cartao: preço normal
- 3x ou mais no cartao: 20% de juros"""

preço = float(input('Qual o valor do produto: '))
pagamento = int(input('Forma de Pagamento.\n Digite: 1- Dinheiro/Cheque | 2- Cartão a vista | '
                      '3- Cartão 2x | 4- 3x ou mais: '))
dinheiro = preço - preço * 0.1
cartao1 = preço - preço * 0.05
cartao2 = preço
cartao3 = preço + preço * 0.2
if pagamento == 1:
    print('Seu produto terá um desconto de 10%. Valor à pagar de R${:.2f}.'.format(dinheiro))
elif pagamento == 2:
    print('Seu produto terá um desconto de 5%. Valor à pagar de R${:.2f}.'.format(cartao1))
elif pagamento == 3:
    print('O valor a pagar é de R${:.2f}. Cada parcela sera de R${:.2f}.'.format(cartao2, cartao2 / 2))
elif pagamento == 4:
    print('O valor total a pagar será de R${:.2f}'.format(cartao3))
    parcela = int(input('Quantas parcelas deseja fazer? '))
    if parcela >= 3:
        print('Sua parcela será de R${:.2f}.'.format(cartao3 / parcela))
else:
    print('Forma de pagamento inválida.')
