print('\033[1;31;40mOlá, Mundo!\033[m')

a = 1
b = 4
print('O valor de a é \033[1;36m{}\033[m e de b é \033[1;31m{}\033[m.'.format(a, b))

nome = 'Raquel'
print('Outra opção de cor é assim. O meu nome é {}{}{}.'.format('\033[1;45m', nome, '\033[m'))

cores = {'limpa' : '\033[m',
         'azul':'\033[36m',
         'p&b':'\033[7;40m', }
print('Meu nome é {}Raquel{}, beijos!'.format(cores['p&b'], cores['limpa']))

x =  'curso de python no cursoemvideo'
print(3*5+4**2)