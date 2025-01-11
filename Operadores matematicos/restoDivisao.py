valor = int(input('Insira um valor: '))

if (valor%2 == 0 and valor > 0):
    print('{} é um número par e positivo' .format(valor))
elif(valor%2 == 0 and valor < 0):
    print('{} é um número par e negativo' .format(valor))
elif(valor%2 != 0 and valor > 0):
    print('{} é um número ímpar e positivo' .format(valor))
elif(valor%2 != 0 and valor < 0):
    print('{} é um número ímpar e negativo' .format(valor))