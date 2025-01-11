valor1 = int(input('Insira o valor 1'))
valor2 = int(input('Insira o valor 2'))
escolhaCalc = str(input('Escolha a operação desejada: (+,-.*,/)'))

if escolhaCalc == '+':
    print(valor1+valor2)
elif escolhaCalc == '-':
    print(valor1-valor2)