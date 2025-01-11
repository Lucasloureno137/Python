pesos = []

for i in range(0,5):
    peso = int(input('Insira seu peso: '))
    pesos.append(peso)

menorPeso = min(pesos)
maiorPeso = max(pesos)

print('O maior peso é {} e o menor é {}'.format(maiorPeso,menorPeso))

