valorAlt = int(input('Insira o valor de altura da parede: '))
valorComp = int(input('Insira o valor de comprimento da parede: '))
valorArea = valorAlt*valorComp
LatasTintaNecessarias = valorArea/2

print('A área da parede é de {} m2 e a quantidade de latas necessárias para pinta-la é de {}'.format(valorArea,LatasTintaNecessarias))