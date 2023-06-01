"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO.
- média entre 5.0 e 6.9: RECUPERAÇÃO.
- média 7.0 ou superior: APROVADO."""

nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Sua média foi {:.1f}. Você foi APROVADO.'.format(media))
elif media < 5:
    print('Sua média foi {:.1f}. Você foi REPROVADO.'.format(media))
else:
    print('Sua média foi {:.1f}. Você está de RECUPERAÇÃO.'.format(media))
