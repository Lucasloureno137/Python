velocidade = int(input('Insira a velocidade medida do veículo: '))

valorMulta = (velocidade - 80) * 7.00

if velocidade > 80:
    print('Você foi multado!!')
else:
    print('Velocidade dentro do permitido')

print(valorMulta)