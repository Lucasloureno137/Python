import math

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa  = math.hypot(catetoOposto,catetoAdjacente)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))


#hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
#print('A medida da hipotenusa é igual a {}' .format(hipotenusa))