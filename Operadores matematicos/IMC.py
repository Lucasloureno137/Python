peso = float(input('Insira seu peso: '))
altura = int(input('Insira sua altura em cm: '))
alturaCmM = altura/100
IMC = peso/(alturaCmM ** 2)

if (IMC <= 18.5):
    print('Você está abaixo do peso')
elif(IMC >= 18.6 and IMC <= 24.9):
    print('Você está no seu peso ideal, parabéns!')
elif(IMC >= 25.0 and IMC <= 29.9):
    print('Você está levemente acima do peso')
elif(IMC >= 30.0 and IMC <= 34.9):
    print('Obesidade grau 1')
elif(IMC >= 35.0 and IMC <= 39.9):
    print('Obesidade grau 2')
elif(IMC >= 40):
    print('Obesidade grau 3')