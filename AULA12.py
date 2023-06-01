nome = str(input('Qual o seu nome? '))
if nome == 'Raquel':
    print('Seu nome é lindo!')
elif nome == 'Joyce' or nome == 'Fátima' or nome == 'Paulo':
    print('Olá {}, seu ultimo nome é Gomes.'.format(nome))
elif nome in 'Glauber Leonardo Luna Sol Cacau':
    print('Olá {}, você faz parte da família de Melo.'.format(nome))
else:
    print('{}, nome é bacana.')
print('Tenha um excelente dia, {}!'.format(nome))
