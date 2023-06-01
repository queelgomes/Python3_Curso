frase = 'Curso em vídeo de Python'
print('Qual a frase que esta na variavel? >>> {}.\n'.format(frase))
print('Quantos itens na frase? >> {} \n'.format(len(frase)))
print('Informar qual valor esta na posição 3 >> {} \n'.format(frase[3]))
print('Informar quais valores estao da posição 3 ate 17 >> {} \n'.format(frase[3:17]))
print('Informar quais valores estao da posição 0 até 17 >> {} \n'.format(frase[:17]))
print('Informar quais valores estão da posição 2 até a 20 pulando de 4 em 4 >> {} \n'.format(frase[2:20:4]))
print('Informar quais valores estao do inicio ate o final pulando de 2 em 2 >> {} \n'.format(frase[::2]))
print('''Aqui esta um texto grande no qual quero escrever,
mas nao quero escrever varios prints,
e quero que va mudando de linha automaticamente.''')
print('Quandos o minusculos aparecem na frase. >> {} \n'.format(frase.count('o')))
print('Colocar a frase em maiuscula e contar quantos caracteres O aparece >>> {}. \n'.format(frase.upper().count('O')))
print('Substituindo palavras >>> {}. \n'.format(frase.replace('Python', 'Java Script')))
print('Onde começa a palavra Python? {} \n'.format(frase.find('Python'))) #mostra em que posicao comecao a string mencionada. Lembrando que a contagem começa do 0.
print('Em que posicao esta a letra o minuscula. >> {} \n'.format(frase.find('o')+1)) #aqui ja mostra como se fosse a gente contando a partir do 1.
print('Em que posicao esta a ultima letra o minuscula. >> {} \n'.format(frase.rfind('o')+1)) #aqui comeca a contagem pela da direita (rigth) se quiser pela esquerda coloca l (left).
print('Tem Python na frase? >> {} \n'.format('Python' in frase)) #aqui da true ou false
print('Aqui mudo uma palavra para minuscula e procuro a posição dela na frase. >> {} \n'.format(frase.lower().find('python'))) #aqui o python na frase esta maiuscula, se eu nao mudar ela para minuscula e fazer a pesquisa, da -1 (nao encontrada). Entao assim eu mudo tudo pra minuscula e acho a palavra.
print('Aqui cada palavra virou um item >> {} \n'.format(frase.split())) #aqui transformou uma lista com cada palavra.
frase2 = '   Olá Mundo    \n'
print(frase2)
print('Aqui remove todos os espaços no inicio e no final. >> {} \n'.format(frase2.strip())) #aqui remove todos os espaços do inicio e fim.
frase3 = frase2.split()
print('Aqui eu junto todos os itens de uma lista e substituo pelo oq esta em aspas >>{}.'.format('***'.join(frase3))) #bom para tirar espaços da string.
numeros = [2, 4, 1, 0]
print(numeros)
print('Aqui vamos colocar na ordem crescente a lista: {}.'.format(sorted(numeros)))
