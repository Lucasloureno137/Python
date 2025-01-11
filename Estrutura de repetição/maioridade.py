contaMaiores = 0
contaMenores = 0

for i in range(0,7):
    anoNasc =int(input('Insira o ano que você nasceu: '))
    
    if 2024 - anoNasc >= 18:
        contaMaiores += 1
    else:
        contaMenores += 1
    
print('O número de maiores de idade é {} e o de menores é {}'.format(contaMaiores,contaMenores))

      
         

    