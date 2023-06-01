n1 = float(input('Qual a sua nota no primeiro semestre? '))
n2 = float(input('Qual a sua nota no segundo semestre? '))
m = (n1+n2)/2
if m < 5:
    print('Sua média é {:.1f}. Você está de recuperação. Estude mais!'.format(m))
else:
    print('Sua média é {:.1f}. Você passou de ano! Parabéns!'.format(m))

print('true' if 1 == 1 else 'false')
