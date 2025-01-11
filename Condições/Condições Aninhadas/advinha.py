import random

listaNumeros = [1 , 2 , 3, 4 , 5]
numeroEscolhido = random.choice(listaNumeros)
escolhaUsuario = int(input('Advinhe o número sorteado de 1-5: '))

if escolhaUsuario == numeroEscolhido:
    print('Você acertou!! O número sorteado foi {}'.format(numeroEscolhido))
else:
    print('Você errou, o número escolhido foi {}'.format(numeroEscolhido))
    
