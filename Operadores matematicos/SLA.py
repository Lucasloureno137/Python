valor1 = int(input('Insira o valor 1: '))
valor2 = int(input('Insira o valor 2: '))
valor3= int(input('Insira o valor 3: '))
soma = valor1+valor2

if(soma < valor3):
    print('Os valores inseridos e somados foram {} e {}, o resultado das somas é de {}, e esse valor é menor que {}' .format(valor1,valor2,soma,valor3))
elif(soma == valor3):
    print('Os valores inseridos e somados foram {} e {}, o resultado das somas é de {}, e esse valor é o mesmo que {}' .format(valor1,valor2,soma,valor3))
else:
        print('Os valores inseridos e somados foram {} e {}, o resultado das somas é de {}, e esse valor é maior que {}' .format(valor1,valor2,soma,valor3))