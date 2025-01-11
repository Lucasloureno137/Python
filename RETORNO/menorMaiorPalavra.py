listaPalavras = []



for i in range(5):
    palavras = str(input('Insira uma palavra'))
    listaPalavras.append(palavras)
print (listaPalavras)

for palavra in listaPalavras:
    print(f"A palavra {palavra} tem {len(palavra)} letras")
    if len(palavra) in listaPalavras > palavra in listaPalavras:
        print(palavra)
    