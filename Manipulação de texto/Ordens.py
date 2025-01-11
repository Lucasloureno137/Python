val1 = int(input('Valor 1: '))
val2 = int(input('Valor 2: '))
val3 = int(input('Valor 3: '))

valores = [val1,val2,val3]

valoresOrdenados = sorted(valores, reverse=False)

print(valoresOrdenados[0],valoresOrdenados[1],valoresOrdenados[2])