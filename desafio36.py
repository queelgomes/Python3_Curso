'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprétimo será negado.'''

financiamento = float(input('Qual o valor do financiamento? R$'))
salario = float(input('Qual o valor do seu salário liquido? R$'))
anos = int(input('Em quanto anos deseja pagar? '))
meses = anos * 12
minimo = salario * 0.3
if financiamento / meses <= minimo:
    print('Financiamento de R${:.2f}.'.format(financiamento))
    print('Salário de R${:.2f}.'.format(salario))
    print('Prazo selecionado de {} meses.'.format(meses))
    print('Empréstimo APROVADO! Sua parcela será de R${:.2f}.'.format(financiamento / meses))
else:
    print('A parcela de R${:.2f} ultrapassa o valor de R${:.2f} do seu salário, que corresponde a 30%.'
          .format(financiamento / meses, minimo))
    print('Empréstimo NEGADO! \nAumente o prazo e faça uma nova simulação.')
