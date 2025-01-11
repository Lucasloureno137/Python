nome = str(input('Insira seu nome: '))

#nome.replace retira os espaços de dentro da frase, em seguida o método len conta os caracteres que restaram
numeroCaracteres = len(nome.replace ('' , ''))
print(nome.upper())
print(nome.lower())
print(numeroCaracteres)
#nome.split divide o texto em segmentos e printa o primeiro segmento([0])
print(nome.split()[0])
