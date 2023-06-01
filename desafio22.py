nome = str(input('Digite o seu nome completo: ')).strip()
nome_maiuscula = nome.upper()
nome_minuscula = nome.lower()
primeiro_nome = nome.split() #criar uma lista com todos os nomes
nome1 = len(primeiro_nome[0])
nome_sem_espaco = ''.join(primeiro_nome)
nome_conta = len(nome_sem_espaco)

print('''Nome em maiúscula: {},
Nome em minúscula: {},
Seu nome tem {} letras e
Seu primeiro nome tem {} letras.'''.format(nome_maiuscula, nome_minuscula, nome_conta, nome1))

print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' '))) #aqui elimino oq esta nos parenteses

print(primeiro_nome)
print(nome_sem_espaco)