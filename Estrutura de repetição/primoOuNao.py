n = int(input('Insira um valor inteiro:'))

if n >1:
    for i in range(2, int(numero**0.5) + 1):
        if n % i == 0:
            print('O número não é primo:')
        else:
            print('O número é primo')