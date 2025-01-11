distanciaViagem = int(input('Insira a distância da viagem: '))

if distanciaViagem <= 200:
    print('O valor da viagem para {}km ficou em: R${}' .format(distanciaViagem,distanciaViagem*0.50))
elif distanciaViagem >= 400:
     print('O valor da viagem para {}km ficou em: R${}' .format(distanciaViagem,distanciaViagem*0.45))