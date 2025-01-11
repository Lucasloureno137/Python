frase = str(input('Digite uma frase: '))
fraseEdit = frase.replace(' ', '').lower()
print(fraseEdit)

if fraseEdit == fraseEdit[::-1]:
    print('A frase é um polindromo')
else:
    print('A frase não é um polindromo')



