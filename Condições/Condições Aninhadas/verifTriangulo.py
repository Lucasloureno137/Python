lado1 = int(input('Insira o valor do lado 1 do triangulo: '))
lado2 = int(input('Insira o valor do lado 2 do triangulo: '))
lado3 = int(input('Insira o valor do lado 3 do triangulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('É possível formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
