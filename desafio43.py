"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade morbida"""

peso = float(input('Qual seu peso atual? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu indice é {:.1f}. Você esta abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu indice é {:.1f}. Você esta no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu indice é {:.1f}. Você esta sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu indice é {:.1f}. Você esta obeso.'.format(imc))
else:
    print('Seu indice é {:.1f}. Você esta com obesidade morbida.'.format(imc))